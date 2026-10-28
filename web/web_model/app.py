# -*- coding: utf-8 -*-
"""
Hệ thống Web Chẩn Đoán Bệnh Cây Trồng Thực Địa & Cây Thanh Long (33 Lớp)
Học phần Khai Phá Dữ Liệu - Khoa CNTT ĐH Thủy Lợi CS2
Nhóm 6: Lê Trí Thiện, Đặng Anh Tường (MSSV: 2351067120), Nguyễn Tuấn Minh
GVHD: ThS. Vũ Thị Hạnh
FastAPI Web Server Backend
"""

import os
import sys
import shutil
import tempfile
import cv2
import json
import numpy as np
from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from model_engine import engine, CLASS_NAMES
from agriculture_knowledge import KNOWLEDGE_BASE

app = FastAPI(
    title="Hệ Thống Chẩn Đoán Bệnh Cây Trồng - KPDL Nhóm 6",
    description="Ứng dụng Khai phá dữ liệu và Thị giác máy tính nhận diện bệnh hại cây trồng thực địa & cây Thanh Long (33 lớp)",
    version="2.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

STATIC_DIR = os.path.join(BASE_DIR, "static")
os.makedirs(STATIC_DIR, exist_ok=True)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

VIDEO_EXTENSIONS = {'.mp4', '.avi', '.mov', '.webm', '.mkv', '.m4v'}
IMAGE_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.bmp', '.tiff'}

@app.get("/", response_class=HTMLResponse)
async def serve_index():
    index_path = os.path.join(STATIC_DIR, "index.html")
    if os.path.exists(index_path):
        with open(index_path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Hệ thống Web KPDL Nhóm 6 đang khởi động... Vui lòng tạo index.html</h1>"

@app.post("/api/diagnose")
async def diagnose_media(file: UploadFile = File(...)):
    """
    Endpoint chẩn đoán chính: Hỗ trợ cả tệp Hình ảnh và Video
    """
    filename = file.filename or "media.jpg"
    ext = os.path.splitext(filename)[1].lower()
    
    is_video = ext in VIDEO_EXTENSIONS
    is_image = ext in IMAGE_EXTENSIONS

    if not is_video and not is_image:
        content_type = file.content_type or ""
        if "video" in content_type:
            is_video = True
            ext = ".mp4"
        else:
            is_image = True
            ext = ".jpg"

    temp_path = None
    try:
        content = await file.read()
        if len(content) == 0:
            raise HTTPException(status_code=400, detail="Tệp tải lên rỗng (0 bytes).")

        if is_image:
            nparr = np.frombuffer(content, np.uint8)
            img_bgr = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            if img_bgr is None:
                raise HTTPException(status_code=400, detail="Không thể giải mã hình ảnh. Vui lòng thử lại tệp ảnh khác.")
            
            result = engine.predict_image(img_bgr)
            result["original_filename"] = filename
            return JSONResponse(content=result)

        else:
            with tempfile.NamedTemporaryFile(delete=False, suffix=ext) as temp_file:
                temp_file.write(content)
                temp_path = temp_file.name

            result = engine.predict_video(temp_path, max_samples=15)
            result["original_filename"] = filename
            return JSONResponse(content=result)

    except HTTPException:
        raise
    except Exception as e:
        import traceback
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={"success": False, "error": f"Lỗi trong quá trình xử lý: {str(e)}"}
        )
    finally:
        if temp_path and os.path.exists(temp_path):
            try:
                os.remove(temp_path)
            except Exception:
                pass

@app.get("/api/system_info")
async def get_system_info():
    """Thông số mô hình và thống kê học phần phục vụ vấn đáp cuối kỳ"""
    metrics_path = os.path.join(BASE_DIR, "metrics.json")
    metrics_data = {}
    if os.path.exists(metrics_path):
        try:
            with open(metrics_path, "r", encoding="utf-8") as f:
                metrics_data = json.load(f)
        except Exception:
            pass

    return {
        "course": "Khai Phá Dữ Liệu (Data Mining) - K65 CNTT",
        "institution": "Trường Đại học Thủy Lợi - Phân hiệu CS2 TP.HCM",
        "instructor": "ThS. Vũ Thị Hạnh (Google Account: Hannah Vu)",
        "team": "Nhóm 6: Lê Trí Thiện, Đặng Anh Tường (MSSV: 2351067120), Nguyễn Tuấn Minh",
        "model": "ResNet18 Transfer Learning (Deep Residual Learning)",
        "classes_count": len(CLASS_NAMES),
        "classes": CLASS_NAMES,
        "dataset_summary": {
            "total_images": 4555,
            "train_set": 3422,
            "val_set": 607,
            "test_set": 526,
            "dark_images_test": 180,
            "dragon_fruit_images": 1900,
            "plantdoc_images": 2655
        },
        "model_comparison": [
            {"model": "Random Forest", "overall_acc": "44.68%", "tl_acc": "60.13%", "plantdoc_acc": "24.00%"},
            {"model": "CNN tự xây", "overall_acc": "52.85%", "tl_acc": "64.78%", "plantdoc_acc": "36.89%"},
            {"model": "ResNet18 Transfer Learning", "overall_acc": "56.08%", "tl_acc": "70.76%", "plantdoc_acc": "36.44%"}
        ],
        "night_enhancement": {
            "status": "Tự động kích hoạt khi độ sáng trung bình < 60",
            "method": "Khử nhiễu Bilateral + Adaptive Gamma + CLAHE",
            "benchmark": "Nâng độ chính xác nhận diện trên ảnh tối lên 20.56% - 26.11%"
        }
    }
