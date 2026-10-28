// ============================================================
// HỆ THỐNG CHẨN ĐOÁN BỆNH CÂY TRỒNG & THANH LONG
// Học phần Khai Phá Dữ Liệu - K65 CNTT - Nhóm 6
// ============================================================

let currentFile = null;

document.addEventListener('DOMContentLoaded', () => {
  initDropzone();
  initDiagnoseButton();
  initModalEvents();
});

// 1. KHỞI TẠO VÙNG TẢI TỆP (CLICK HOẶC KÉO THẢ)
function initDropzone() {
  const dropzone = document.getElementById('dropzone');
  const mediaInput = document.getElementById('mediaInput');
  const btnRemove = document.getElementById('btnRemoveFile');

  // Kéo thả events
  ['dragenter', 'dragover'].forEach(eventName => {
    dropzone.addEventListener(eventName, (e) => {
      e.preventDefault();
      e.stopPropagation();
      dropzone.classList.add('dragover');
    });
  });

  ['dragleave', 'drop'].forEach(eventName => {
    dropzone.addEventListener(eventName, (e) => {
      e.preventDefault();
      e.stopPropagation();
      dropzone.classList.remove('dragover');
    });
  });

  dropzone.addEventListener('drop', (e) => {
    const dt = e.dataTransfer;
    if (dt && dt.files && dt.files.length > 0) {
      handleSelectedFile(dt.files[0]);
    }
  });

  // Chọn từ input
  mediaInput.addEventListener('change', (e) => {
    if (e.target.files && e.target.files.length > 0) {
      handleSelectedFile(e.target.files[0]);
    }
  });

  // Nút đổi tệp khác
  btnRemove.addEventListener('click', (e) => {
    e.stopPropagation();
    resetUploadState();
    mediaInput.click();
  });
}

function handleSelectedFile(file) {
  currentFile = file;
  const isVideo = file.type.startsWith('video/') || /\.(mp4|avi|mov|webm|mkv)$/i.test(file.name);
  const isImage = file.type.startsWith('image/') || /\.(jpg|jpeg|png|webp|bmp)$/i.test(file.name);

  if (!isVideo && !isImage) {
    alert("Vui lòng chọn tệp hình ảnh (.jpg, .png, .webp) hoặc video (.mp4, .webm, .mov)!");
    return;
  }

  const promptEl = document.getElementById('dropzonePrompt');
  const previewWrapper = document.getElementById('previewWrapper');
  const previewImg = document.getElementById('previewImg');
  const previewVideo = document.getElementById('previewVideo');
  const nameEl = document.getElementById('previewFileName');
  const typeEl = document.getElementById('previewFileType');
  const btnDiagnose = document.getElementById('btnDiagnose');

  promptEl.style.display = 'none';
  previewWrapper.style.display = 'flex';
  nameEl.textContent = file.name;

  if (isImage) {
    typeEl.textContent = "Ảnh thực địa";
    typeEl.style.color = "var(--emerald-light)";
    previewVideo.style.display = 'none';
    previewVideo.pause();

    const reader = new FileReader();
    reader.onload = (e) => {
      previewImg.src = e.target.result;
      previewImg.style.display = 'block';
    };
    reader.readAsDataURL(file);
  } else {
    typeEl.textContent = "Video quay cành";
    typeEl.style.color = "var(--accent-gold)";
    previewImg.style.display = 'none';

    const videoUrl = URL.createObjectURL(file);
    previewVideo.src = videoUrl;
    previewVideo.style.display = 'block';
  }

  btnDiagnose.disabled = false;
  btnDiagnose.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

function resetUploadState() {
  currentFile = null;
  document.getElementById('mediaInput').value = '';
  document.getElementById('dropzonePrompt').style.display = 'flex';
  document.getElementById('previewWrapper').style.display = 'none';
  
  const img = document.getElementById('previewImg');
  img.src = '';
  img.style.display = 'none';

  const video = document.getElementById('previewVideo');
  video.pause();
  video.src = '';
  video.style.display = 'none';

  document.getElementById('btnDiagnose').disabled = true;
}

// 2. THỰC HIỆN CHẨN ĐOÁN & GỌI API
function initDiagnoseButton() {
  const btn = document.getElementById('btnDiagnose');
  btn.addEventListener('click', executeDiagnosis);
}

async function executeDiagnosis() {
  if (!currentFile) {
    alert("Vui lòng chọn ảnh hoặc video trước khi bấm chẩn đoán!");
    return;
  }

  const loadingOverlay = document.getElementById('loadingOverlay');
  loadingOverlay.style.display = 'flex';

  const formData = new FormData();
  formData.append('file', currentFile);

  try {
    const response = await fetch('/api/diagnose', {
      method: 'POST',
      body: formData
    });

    const data = await response.json();
    loadingOverlay.style.display = 'none';

    if (!response.ok || !data.success) {
      alert("Lỗi chẩn đoán: " + (data.error || "Không thể phân tích dữ liệu."));
      return;
    }

    // Hiển thị kết quả chi tiết lên Modal
    renderResultModal(data);

  } catch (error) {
    loadingOverlay.style.display = 'none';
    alert("Đã xảy ra lỗi kết nối máy chủ: " + error.message);
  }
}

// 3. ĐỔ DỮ LIỆU LÊN MODAL KẾT QUẢ TOÀN DIỆN
function renderResultModal(data) {
  // Tiêu đề & Badges
  document.getElementById('modalDiseaseTitle').textContent = data.disease_name_vi;
  document.getElementById('modalDiseaseEn').textContent = data.disease_name_en;
  
  const plantBadge = document.getElementById('modalPlantType');
  plantBadge.textContent = data.plant_type.toUpperCase();

  const statusBadge = document.getElementById('modalStatusBadge');
  statusBadge.textContent = data.status_text;
  statusBadge.style.backgroundColor = data.badge_color + '25';
  statusBadge.style.color = data.badge_color;
  statusBadge.style.borderColor = data.badge_color + '60';

  // Night Mode Badge
  const nightBadge = document.getElementById('modalNightBadge');
  if (data.night_mode) {
    nightBadge.style.display = 'inline-block';
  } else {
    nightBadge.style.display = 'none';
  }

  // Khung hình & Latency
  const previewImg = document.getElementById('modalPreviewImg');
  previewImg.src = data.preview_image;

  document.getElementById('modalMediaTag').textContent = data.is_video ? "Video Đã Quét" : "Ảnh Thực Địa";
  document.getElementById('modalInferenceTime').textContent = `⚡ ${data.inference_time_ms} ms`;

  // Độ tin cậy (Confidence)
  const percentEl = document.getElementById('modalConfidencePercent');
  const barEl = document.getElementById('modalConfidenceBar');
  const descEl = document.getElementById('modalConfidenceDesc');

  percentEl.textContent = data.confidence_percent + '%';
  barEl.style.width = data.confidence_percent + '%';

  if (data.confidence_percent >= 85) {
    descEl.textContent = "Độ tin cậy rất cao";
    percentEl.style.color = "var(--emerald-light)";
  } else if (data.confidence_percent >= 60) {
    descEl.textContent = "Độ tin cậy khá";
    percentEl.style.color = "var(--accent-gold)";
  } else {
    descEl.textContent = "Cần theo dõi thêm";
    percentEl.style.color = "#f87171";
  }

  // Nếu là Video
  const bestFrameBar = document.getElementById('modalBestFrameBar');
  const videoSummaryBox = document.getElementById('modalVideoSummaryBox');
  const videoTimelineBox = document.getElementById('modalVideoTimelineBox');

  if (data.is_video) {
    bestFrameBar.style.display = 'block';
    document.getElementById('modalBestTimestamp').textContent = data.best_timestamp || "00:01";

    videoSummaryBox.style.display = 'block';
    document.getElementById('modalVideoFrames').textContent = data.total_frames_sampled;
    document.getElementById('modalVideoDuration').textContent = data.video_duration_sec;
    document.getElementById('modalVideoConsensus').textContent = data.consensus_rate + '%';

    // Đổ timeline các frame
    videoTimelineBox.style.display = 'block';
    const timelineBody = document.getElementById('modalTimelineBody');
    timelineBody.innerHTML = '';
    (data.timeline || []).forEach(frame => {
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td><strong>${frame.time_str}</strong></td>
        <td>Khung #${frame.frame_idx}</td>
        <td>${frame.predicted_vi}</td>
        <td style="color: var(--emerald-light); font-weight:700;">${frame.confidence}%</td>
      `;
      timelineBody.appendChild(tr);
    });

  } else {
    bestFrameBar.style.display = 'none';
    videoSummaryBox.style.display = 'none';
    videoTimelineBox.style.display = 'none';
  }

  // Top-3 Phân phối
  const top3Container = document.getElementById('modalTop3List');
  top3Container.innerHTML = '';
  data.top3.forEach(item => {
    const itemEl = document.createElement('div');
    itemEl.className = 'top3-item';
    itemEl.innerHTML = `
      <div class="top3-info">
        <span class="top3-name">${item.name_vi}</span>
        <span class="top3-val">${item.probability}%</span>
      </div>
      <div class="top3-bar-bg">
        <div class="top3-bar-fill" style="width: ${item.probability}%;"></div>
      </div>
    `;
    top3Container.appendChild(itemEl);
  });

  // Triệu chứng
  const symptomsList = document.getElementById('modalSymptomsList');
  symptomsList.innerHTML = '';
  data.symptoms.forEach(sym => {
    const li = document.createElement('li');
    li.textContent = sym;
    symptomsList.appendChild(li);
  });

  // Khuyến nghị canh tác & Bảng thuốc
  const treatmentText = document.getElementById('modalTreatmentCanhTac');
  treatmentText.innerHTML = `
    <strong>Biện pháp canh tác:</strong> ${data.treatment.canh_tac}<br><br>
    <strong>Chế độ dinh dưỡng:</strong> ${data.treatment.dinh_duong}<br><br>
    <strong>Phòng ngừa:</strong> ${data.treatment.phong_ngua}
  `;

  const drugsContainer = document.getElementById('modalDrugsContainer');
  const drugsTbody = document.getElementById('modalDrugsTableBody');
  drugsTbody.innerHTML = '';

  if (data.drugs && data.drugs.length > 0) {
    drugsContainer.style.display = 'block';
    data.drugs.forEach(drug => {
      const tr = document.createElement('tr');
      tr.innerHTML = `
        <td><strong>${drug.name}</strong></td>
        <td><span style="color: var(--accent-gold); font-family: monospace;">${drug.active}</span></td>
        <td>${drug.dose}</td>
      `;
      drugsTbody.appendChild(tr);
    });
  } else {
    drugsContainer.style.display = 'none';
  }

  // Mở modal
  openModal();
}

// 4. ĐÓNG / MỞ MODAL
function openModal() {
  const modal = document.getElementById('resultModal');
  modal.style.display = 'flex';
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  const modal = document.getElementById('resultModal');
  modal.style.display = 'none';
  document.body.style.overflow = 'auto';
}

function initModalEvents() {
  document.getElementById('btnCloseModal').addEventListener('click', closeModal);

  // Bấm ra ngoài vùng modal container
  document.getElementById('resultModal').addEventListener('click', (e) => {
    if (e.target.id === 'resultModal') {
      closeModal();
    }
  });

  // Bấm phím Escape
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
      closeModal();
    }
  });
}
