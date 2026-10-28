# -*- coding: utf-8 -*-
"""
Bộ máy Suy diễn & Tiền xử lý Ảnh / Video Chuyên sâu - 33 Lớp
Học phần Khai Phá Dữ Liệu - Khoa CNTT ĐH Thủy Lợi CS2 - Nhóm 6
Tích hợp BoNhanDien từ predict.py với cơ sở dữ liệu nông nghiệp 33 lớp
"""
import os
import sys
import time
import base64
import json
import cv2
import numpy as np
from PIL import Image
from typing import Dict, Any, List

# Tìm thư mục chứa model và config
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CANDIDATE_DIRS = [
    CURRENT_DIR,
    r"A:\KPDL\web_model-20261028T011432Z-1-001_hoanchinh\web_model",
]

MODEL_DIR = None
for c in CANDIDATE_DIRS:
    if os.path.exists(os.path.join(c, "config.json")) and os.path.exists(os.path.join(c, "model_torchscript.pt")):
        MODEL_DIR = c
        break

if MODEL_DIR is None:
    MODEL_DIR = CURRENT_DIR

if MODEL_DIR not in sys.path:
    sys.path.insert(0, MODEL_DIR)

from predict import BoNhanDien
from agriculture_knowledge import get_disease_info

class ModelEngine:
    def __init__(self, model_dir=MODEL_DIR):
        self.model_dir = model_dir
        self.bo = BoNhanDien(model_dir)
        self.classes = self.bo.cfg.get('classes', [])
        print(f"[ModelEngine] Loaded BoNhanDien successfully with {len(self.classes)} classes from {model_dir}")

    def predict_image(self, img_bgr: np.ndarray) -> Dict[str, Any]:
        t0 = time.time()
        # Chuyển BGR sang RGB cho PIL
        img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(img_rgb)

        # Suy diễn qua BoNhanDien (lấy top 3)
        res = self.bo.du_doan_anh(pil_img, top=3)
        inference_time_ms = round((time.time() - t0) * 1000, 2)

        ket_qua = res.get('ket_qua', [])
        da_lam_sang = bool(res.get('da_lam_sang', False))

        if not ket_qua:
            raise ValueError("Không nhận được kết quả dự đoán từ mô hình.")

        top_item = ket_qua[0]
        top_class = top_item['lop']
        top_prob = float(top_item['xac_suat'])

        # Lấy thông tin nông nghiệp từ agriculture_knowledge
        disease_info = get_disease_info(top_class)

        # Top 3
        top3 = []
        for item in ket_qua[:3]:
            c_name = item['lop']
            c_info = get_disease_info(c_name)
            top3.append({
                "class_en": c_name,
                "name_vi": c_info["short_name"],
                "probability": round(float(item['xac_suat']) * 100, 1),
                "is_dragon_fruit": item.get('la_thanh_long', False)
            })

        # Tạo ảnh xem trước base64
        _, buffer = cv2.imencode('.jpg', img_bgr, [cv2.IMWRITE_JPEG_QUALITY, 85])
        preview_b64 = "data:image/jpeg;base64," + base64.b64encode(buffer).decode('utf-8')

        return {
            "success": True,
            "is_video": False,
            "disease_name_vi": disease_info["name_vi"],
            "disease_name_en": disease_info["name_en"],
            "short_name": disease_info["short_name"],
            "plant_type": disease_info["plant_type"],
            "status_level": disease_info["status_level"],
            "status_text": disease_info["status_text"],
            "badge_color": disease_info["badge_color"],
            "confidence_percent": round(top_prob * 100, 1),
            "top3": top3,
            "night_mode": da_lam_sang,
            "symptoms": disease_info["symptoms"],
            "treatment": disease_info["treatment"],
            "drugs": disease_info["drugs"],
            "inference_time_ms": inference_time_ms,
            "preview_image": preview_b64,
            "model_architecture": "ResNet18 Transfer Learning (TorchScript 33 Lớp)"
        }

    def predict_video(self, video_path: str, max_samples: int = 15) -> Dict[str, Any]:
        t0 = time.time()
        cap = cv2.VideoCapture(video_path)
        if not cap.isOpened():
            return {"success": False, "error": "Không thể mở tệp video. Định dạng không hợp lệ hoặc tệp bị hỏng."}

        fps = cap.get(cv2.CAP_PROP_FPS) or 30.0
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        duration_sec = round(total_frames / fps, 2) if total_frames > 0 else 0.0
        cap.release()

        # Suy diễn video qua BoNhanDien
        res = self.bo.du_doan_video(video_path, moi_giay=1, toi_da=max_samples, top=3)
        inference_time_ms = round((time.time() - t0) * 1000, 2)

        ket_qua = res.get('ket_qua', [])
        khung = res.get('khung', [])
        so_khung = res.get('so_khung', len(khung))

        if not ket_qua:
            return {"success": False, "error": "Không có khung hình nào được phân tích thành công."}

        top_item = ket_qua[0]
        final_class = top_item['lop']
        final_prob = float(top_item['xac_suat'])
        disease_info = get_disease_info(final_class)

        timeline = []
        best_timestamp = 0.0
        highest_conf = -1.0
        winner_votes = 0
        night_mode_detected = False
        best_frame_idx = 0

        for idx, k in enumerate(khung):
            c_name = k.get('lop', '')
            prob = float(k.get('xac_suat', 0.0))
            sec = float(k.get('giay', 0.0))
            if k.get('da_lam_sang', False):
                night_mode_detected = True
            if c_name == final_class:
                winner_votes += 1
            if prob > highest_conf:
                highest_conf = prob
                best_timestamp = sec
                best_frame_idx = int(round(sec * fps))

            c_info = get_disease_info(c_name)
            timeline.append({
                "frame_idx": idx + 1,
                "timestamp_sec": sec,
                "time_str": f"{int(sec // 60):02d}:{int(sec % 60):02d}",
                "predicted_class": c_name,
                "predicted_vi": c_info["short_name"],
                "confidence": round(prob * 100, 1)
            })

        consensus_rate = round((winner_votes / max(len(khung), 1)) * 100, 1)

        # Trích xuất best keyframe
        keyframe_b64 = ""
        cap = cv2.VideoCapture(video_path)
        if cap.isOpened():
            cap.set(cv2.CAP_PROP_POS_FRAMES, best_frame_idx)
            ret, frame = cap.read()
            if ret and frame is not None:
                _, buffer = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, 85])
                keyframe_b64 = "data:image/jpeg;base64," + base64.b64encode(buffer).decode('utf-8')
            cap.release()

        # Top 3
        top3 = []
        for item in ket_qua[:3]:
            c_name = item['lop']
            c_info = get_disease_info(c_name)
            top3.append({
                "class_en": c_name,
                "name_vi": c_info["short_name"],
                "probability": round(float(item['xac_suat']) * 100, 1),
                "is_dragon_fruit": item.get('la_thanh_long', False)
            })

        return {
            "success": True,
            "is_video": True,
            "disease_name_vi": disease_info["name_vi"],
            "disease_name_en": disease_info["name_en"],
            "short_name": disease_info["short_name"],
            "plant_type": disease_info["plant_type"],
            "status_level": disease_info["status_level"],
            "status_text": disease_info["status_text"],
            "badge_color": disease_info["badge_color"],
            "confidence_percent": round(final_prob * 100, 1),
            "consensus_rate": consensus_rate,
            "total_frames_sampled": so_khung,
            "video_duration_sec": duration_sec,
            "best_timestamp": f"{int(best_timestamp // 60):02d}:{int(best_timestamp % 60):02d}",
            "top3": top3,
            "night_mode": night_mode_detected,
            "symptoms": disease_info["symptoms"],
            "treatment": disease_info["treatment"],
            "drugs": disease_info["drugs"],
            "preview_image": keyframe_b64,
            "timeline": timeline,
            "inference_time_ms": inference_time_ms,
            "model_architecture": "ResNet18 Temporal Sampling (TorchScript 33 Lớp)"
        }

engine = ModelEngine()
CLASS_NAMES = engine.classes
