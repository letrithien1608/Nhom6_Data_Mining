# Nhan dien benh la cay / canh thanh long cho web - Nhom 6
# Cach dung:
#   from predict import BoNhanDien
#   bo = BoNhanDien('web_model')               # thu muc chua config.json va model_torchscript.pt
#   bo.du_doan_anh('anh.jpg')                  # hoac truyen vao PIL Image
#   bo.du_doan_video('video.mp4')
import os, json
import numpy as np
import cv2
import torch
from PIL import Image


class BoNhanDien:
    def __init__(self, thu_muc):
        with open(os.path.join(thu_muc, 'config.json'), encoding='utf-8') as f:
            self.cfg = json.load(f)
        self.model = torch.jit.load(os.path.join(thu_muc, 'model_torchscript.pt'), map_location='cpu').eval()
        self.mean = np.array(self.cfg['mean'], dtype=np.float32)
        self.std = np.array(self.cfg['std'], dtype=np.float32)

    def _resize(self, img):
        canh = self.cfg['resize_canh_ngan']
        w, h = img.size
        tl = canh / min(w, h)
        return img.resize((max(canh, round(w * tl)), max(canh, round(h * tl))), Image.BILINEAR)

    def _lam_sang(self, img):
        ls, cach = self.cfg['lam_sang'], self.cfg['cach_lam_sang']
        a = np.asarray(img.convert('RGB'))
        if 'Khu nhieu' in cach:
            d, sc, ss = ls['bilateral']
            a = cv2.bilateralFilter(a, d, sc, ss)
        if 'Gamma' in cach:
            f = a.astype(np.float32) / 255
            tb = max(float(f.mean()), 1e-3)
            if tb < ls['gamma_muc_tieu']:
                g = float(np.clip(np.log(ls['gamma_muc_tieu']) / np.log(tb), ls['gamma_min'], 1.0))
                f = np.power(f, g)
            a = (f * 255).clip(0, 255).astype(np.uint8)
        if 'CLAHE' in cach:
            lab = cv2.cvtColor(a, cv2.COLOR_RGB2LAB)
            o = ls['clahe_o']
            lab[..., 0] = cv2.createCLAHE(clipLimit=ls['clahe_clip'], tileGridSize=(o, o)).apply(lab[..., 0])
            a = cv2.cvtColor(lab, cv2.COLOR_LAB2RGB)
        return Image.fromarray(a)

    def _chuan_bi(self, img):
        img = self._resize(img.convert('RGB'))
        toi = float(np.asarray(img.convert('L')).mean()) < self.cfg['nguong_lam_sang']
        if toi:
            img = self._lam_sang(img)
        c = self.cfg['center_crop']
        w, h = img.size
        l, t = int(round((w - c) / 2.0)), int(round((h - c) / 2.0))
        x = (np.asarray(img.crop((l, t, l + c, t + c)), dtype=np.float32) / 255 - self.mean) / self.std
        return torch.from_numpy(x.transpose(2, 0, 1).copy()), toi

    def _top(self, prob, top):
        idx = np.argsort(prob)[::-1][:top]
        return [{'lop': self.cfg['classes'][i], 'xac_suat': round(float(prob[i]), 4),
                 'la_thanh_long': self.cfg['classes'][i] in self.cfg['nhom_lop']['thanh_long']} for i in idx]

    @torch.no_grad()
    def du_doan_anh(self, img, top=3):
        if isinstance(img, str):
            img = Image.open(img)
        x, toi = self._chuan_bi(img)
        prob = torch.softmax(self.model(x.unsqueeze(0)), 1)[0].numpy()
        return {'ket_qua': self._top(prob, top), 'da_lam_sang': toi}

    @torch.no_grad()
    def du_doan_video(self, path, moi_giay=None, toi_da=None, top=3):
        moi_giay = moi_giay or self.cfg['video']['moi_giay']
        toi_da = toi_da or self.cfg['video']['toi_da_khung']
        cap = cv2.VideoCapture(path)
        n, fps = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)), cap.get(cv2.CAP_PROP_FPS) or 30
        vi_tri = np.arange(0, max(n, 1), max(1, int(round(fps / moi_giay))))
        if len(vi_tri) > toi_da:
            vi_tri = vi_tri[np.linspace(0, len(vi_tri) - 1, toi_da).astype(int)]
        xs, khung = [], []
        for i in vi_tri:
            cap.set(cv2.CAP_PROP_POS_FRAMES, int(i))
            ok, f = cap.read()
            if not ok:
                continue
            x, toi = self._chuan_bi(Image.fromarray(cv2.cvtColor(f, cv2.COLOR_BGR2RGB)))
            xs.append(x)
            khung.append({'giay': round(float(i / fps), 2), 'da_lam_sang': toi})
        cap.release()
        if not xs:
            return {'ket_qua': [], 'so_khung': 0, 'khung': []}
        prob = torch.softmax(self.model(torch.stack(xs)), 1).numpy()
        for k, p in zip(khung, prob):
            j = int(p.argmax())
            k.update({'lop': self.cfg['classes'][j], 'xac_suat': round(float(p[j]), 4)})
        return {'ket_qua': self._top(prob.mean(0), top), 'so_khung': len(khung), 'khung': khung}
