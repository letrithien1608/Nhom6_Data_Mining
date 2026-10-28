@echo off
chcp 65001 >nul
title HE THONG CHAN DOAN BENH CAY TRONG - KPDL NHOM 6
echo ======================================================================
echo    TRUONG DAI HOC THUY LOI - CO SO 2 TP. HO CHI MINH
echo    HOC PHAN: KHAI PHA DU LIEU (DATA MINING) - K65 CNTT
echo    NHOM 6: Le Tri Thien - Dang Anh Tuong (2351067120) - Nguyen Tuan Minh
echo ======================================================================
echo.
echo [*] Dang khoi dong Web Chan Doan Benh Cay Trong va Thanh Long...
echo [*] Vui long doi vai giay de nap mo hinh, trinh duyet se tu mo.
cd /d "%~dp0"

rem Mo trinh duyet sau 15 giay de server kip nap mo hinh
start "" /min cmd /c "timeout /t 15 /nobreak >nul & start "" http://localhost:8000"
python -m uvicorn app:app --host 127.0.0.1 --port 8000
pause
