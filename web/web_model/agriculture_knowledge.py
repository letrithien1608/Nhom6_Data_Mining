# -*- coding: utf-8 -*-
"""
Hệ thống Cơ sở Tri thức Nông nghiệp & Dược liệu Bảo vệ Thực vật - 33 LỚP TOÀN DIỆN
Bao gồm:
- 6 trạng thái bệnh cành cây Thanh Long (Bản địa Việt Nam)
- 27 trạng thái bệnh hại trên 12 loài cây trồng thực địa (Bộ dữ liệu PlantDoc)
Học phần Khai Phá Dữ Liệu - Khoa CNTT ĐH Thủy Lợi CS2 - Nhóm 6
"""

KNOWLEDGE_BASE = {
    # =========================================================================
    # 1. CÂY THANH LONG (6 LỚP)
    # =========================================================================
    "Dragon fruit healthy": {
        "name_en": "Dragon fruit healthy",
        "name_vi": "Cây Thanh Long: Cành Khỏe Mạnh",
        "short_name": "Thanh Long Khỏe Mạnh",
        "plant_type": "Cây Thanh Long (Hylocereus undatus)",
        "status_level": "safe",
        "status_text": "CÀNH KHỎE MẠNH - SINH TRƯỞNG TỐT",
        "badge_color": "#10b981",
        "symptoms": [
            "Cành thanh long có màu xanh lục tươi đến xanh sẫm đồng nhất, lớp biểu bì căng bóng, mọng nước.",
            "Gờ cành dày dặn, không có vết đốm vàng, chấm nấm trắng, vệt hoại tử hay vùng mô thối nhũn.",
            "Mắt gai lành lặn, chuẩn bị phát triển chồi non hoặc nụ hoa bình thường."
        ],
        "treatment": {
            "canh_tac": "Tưới nước nhỏ giọt hoặc tưới gốc, tránh tưới phun mưa lúc chiều tối để giảm ẩm độ tán cành. Bón phân hữu cơ hoai mục ủ nấm Trichoderma định kỳ.",
            "dinh_duong": "Bón phân N-P-K cân đối, bổ sung Canxi-Bo định kỳ giúp vách tế bào cành dày và cứng cáp.",
            "phong_ngua": "Tỉa bỏ cành già, cành khuất sáng bên trong tán để tạo thông thoáng hình nấm tròn."
        },
        "drugs": []
    },

    "Dragon fruit red fungus": {
        "name_en": "Dragon fruit red fungus",
        "name_vi": "Cây Thanh Long: Bệnh Nấm Đỏ",
        "short_name": "Thanh Long: Nấm Đỏ",
        "plant_type": "Cây Thanh Long (Hylocereus undatus)",
        "status_level": "danger",
        "status_text": "BỆNH NGUY HIỂM - CẦN PHUN THUỐC SỚM",
        "badge_color": "#ef4444",
        "symptoms": [
            "Xuất hiện các chấm nhỏ màu đỏ gạch hoặc đỏ cam sần sùi trên lớp biểu bì vỏ cành.",
            "Vết bệnh phát triển gồ lên mặt cành, sau đó liên kết thành mảng lớn màu nâu đỏ đến tím thẫm.",
            "Biểu bì cành bị chai cứng, nứt nẻ, làm suy giảm nghiêm trọng khả năng quang hợp và teo cành."
        ],
        "treatment": {
            "canh_tac": "Cắt tỉa cành bệnh nặng đem ra ngoài vườn tiêu hủy; khử trùng dụng cụ cắt tỉa bằng cồn hoặc nước vôi.",
            "dinh_duong": "Tạm dừng bón thừa phân đạm; tăng cường Kali và Lân hữu cơ để nâng cao sức đề kháng.",
            "phong_ngua": "Phun phòng ngừa toàn bộ trụ cây vào đầu mùa mưa hoặc sau các đợt sương mù kéo dài."
        },
        "drugs": [
            {"name": "Champion 77WP", "active": "Copper Hydroxide", "dose": "30g / bình 16 lít"},
            {"name": "Coc 85WP", "active": "Copper Oxychloride", "dose": "25-30g / bình 16 lít"},
            {"name": "Anvil 5SC", "active": "Hexaconazole", "dose": "20ml / bình 16 lít"},
            {"name": "Ridomil Gold 68WG", "active": "Metalaxyl-M + Mancozeb", "dose": "50g / bình 16 lít"}
        ]
    },

    "Dragon fruit yellow spot": {
        "name_en": "Dragon fruit yellow spot",
        "name_vi": "Cây Thanh Long: Bệnh Đốm Vàng",
        "short_name": "Thanh Long: Đốm Vàng",
        "plant_type": "Cây Thanh Long (Hylocereus undatus)",
        "status_level": "warning",
        "status_text": "CẢNH BÁO - NGUY CƠ LÂY LAN TRÊN CÀNH",
        "badge_color": "#f59e0b",
        "symptoms": [
            "Các chấm tròn nhỏ màu vàng nhạt li ti phân tán rải rác trên các gờ phiến cành.",
            "Ở giai đoạn chớm bệnh, vết đốm vàng làm mất diệp lục; khi ẩm độ cao, đốm vàng mở rộng và lõm nhẹ.",
            "Thường phát sinh mạnh khi thời tiết ẩm ướt hoặc đất quanh trụ cây bị ngập úng nhẹ."
        ],
        "treatment": {
            "canh_tac": "Khơi thông rãnh thoát nước quanh trụ cây, dọn sạch cỏ gốc không để ẩm độ đọng dưới chân trụ.",
            "dinh_duong": "Phun phân bón lá chứa trung vi lượng Canxi, Magie, Kẽm để phục hồi diệp lục.",
            "phong_ngua": "Phun thuốc gốc nấm phổ rộng khi phát hiện các chấm vàng bắt đầu xuất hiện trên cành non."
        },
        "drugs": [
            {"name": "Score 250EC", "active": "Difenoconazole", "dose": "10-15ml / bình 16 lít"},
            {"name": "Tilt Super 300EC", "active": "Difenoconazole + Propiconazole", "dose": "10ml / bình 16 lít"},
            {"name": "Amistar Top 325SC", "active": "Azoxystrobin + Difenoconazole", "dose": "15ml / bình 16 lít"}
        ]
    },

    "Dragon fruit coin spot": {
        "name_en": "Dragon fruit coin spot",
        "name_vi": "Cây Thanh Long: Bệnh Nấm Đồng Tiền (Đốm Trắng)",
        "short_name": "Thanh Long: Nấm Đồng Tiền",
        "plant_type": "Cây Thanh Long (Hylocereus undatus)",
        "status_level": "danger",
        "status_text": "BỆNH DỊCH PHỔ BIẾN - CẦN PHUN THUỐC NGAY",
        "badge_color": "#dc2626",
        "symptoms": [
            "Vết bệnh đặc trưng hình tròn hoặc bầu dục lõm nhẹ, viền nổi gờ rõ rệt giống hình đồng tiền xu.",
            "Tâm vết bệnh màu trắng xám tro hoặc xám bạc, bao quanh bởi một vòng viền nâu sẫm đến vàng cam.",
            "Bệnh phát triển cực mạnh trong mùa mưa ẩm, làm sượng trái, teo cành và rụng hoa non."
        ],
        "treatment": {
            "canh_tac": "Cắt tỉa cành tạo tán hình nấm thông thoáng; thu gom cành bệnh đem chôn hoặc đốt tiêu hủy.",
            "dinh_duong": "Tăng cường phân lân và kali hữu cơ, hạn chế bón thừa đạm trong mùa dịch bệnh.",
            "phong_ngua": "Phun luân phiên 2-3 loại hoạt chất để tránh hiện tượng nấm bệnh kháng thuốc."
        },
        "drugs": [
            {"name": "Amistar Top 325SC", "active": "Azoxystrobin + Difenoconazole", "dose": "15-20ml / bình 16 lít"},
            {"name": "Nativo 750WG", "active": "Tebuconazole + Trifloxystrobin", "dose": "6-8g / bình 16 lít"},
            {"name": "Antracol 70WP", "active": "Propineb", "dose": "50g / bình 16 lít"},
            {"name": "Ridomil Gold 68WG", "active": "Metalaxyl-M + Mancozeb", "dose": "50g / bình 16 lít"}
        ]
    },

    "Dragon fruit streak spot": {
        "name_en": "Dragon fruit streak spot",
        "name_vi": "Cây Thanh Long: Bệnh Đốm Dây (Vệt Nâu Dài)",
        "short_name": "Thanh Long: Đốm Dây",
        "plant_type": "Cây Thanh Long (Hylocereus undatus)",
        "status_level": "warning",
        "status_text": "BỆNH CẢNH BÁO - LÂY LAN THEO GỜ CÀNH",
        "badge_color": "#d97706",
        "symptoms": [
            "Các vết hoại tử màu nâu liên kết nhau tạo thành vệt sọc dài chạy dọc theo các gờ cành hoặc mép gai.",
            "Bề mặt vệt bệnh khô ráp, chuyển sang màu xám đen, cản trở sự vận chuyển nhựa nuôi cành.",
            "Cành bị bệnh thường còi cọc, giảm khả năng đậu hoa và nuôi dưỡng trái non."
        ],
        "treatment": {
            "canh_tac": "Tránh gây xây xát hoặc vết thương hở khi buộc cành cố định trụ; cắt bỏ cành có vệt nâu chiếm >50% chiều dài.",
            "dinh_duong": "Bón phân hữu cơ khoáng vi sinh để kích thích rễ phát triển khỏe, cành phục hồi nhanh.",
            "phong_ngua": "Phun phòng ngừa sau các đợt cắt tỉa cành hoặc sau các trận mưa dầm bão lớn."
        },
        "drugs": [
            {"name": "Daconil 75WP", "active": "Chlorothalonil", "dose": "30g / bình 16 lít"},
            {"name": "Bravo 720SC", "active": "Chlorothalonil", "dose": "20ml / bình 16 lít"},
            {"name": "Amistar 250SC", "active": "Azoxystrobin", "dose": "15ml / bình 16 lít"}
        ]
    },

    "Dragon fruit stem rot": {
        "name_en": "Dragon fruit stem rot",
        "name_vi": "Cây Thanh Long: Bệnh Thối Cành (Thối Nhũn)",
        "short_name": "Thanh Long: Thối Cành",
        "plant_type": "Cây Thanh Long (Hylocereus undatus)",
        "status_level": "danger",
        "status_text": "NGHIÊM TRỌNG - NGUY CƠ CHẾT CÀNH NHANH",
        "badge_color": "#991b1b",
        "symptoms": [
            "Mô thịt cành bị úng nước, đổi màu vàng nâu đến nâu đen, mềm nhũn và bốc mùi chua hôi đặc trưng.",
            "Vết thối lan cực nhanh dọc thân cành do nấm kết hợp vi khuẩn Erwinia carotovora tấn công.",
            "Phần thịt cành rữa nát chỉ còn trơ lại sợi lõi gỗ bên trong, làm toàn bộ phần ngọn phía trên héo rụng."
        ],
        "treatment": {
            "canh_tac": "Dùng dao sắc đã tiệt trùng cắt bỏ ngay phần thối lùi sâu vào phần cành lành 3-5 cm. Bôi vôi đặc hoặc thuốc sát trùng vào vết cắt.",
            "dinh_duong": "Ngưng tưới nước và ngưng toàn bộ phân bón gốc cho đến khi vết thương khô ráo hẳn.",
            "phong_ngua": "Khơi thông rãnh thoát nước giữa các hàng trụ, dọn sạch cỏ gốc không để ẩm ướt."
        },
        "drugs": [
            {"name": "Kasuran 47WP", "active": "Kasugamycin + Copper Oxychloride", "dose": "30-40g / bình 16 lít"},
            {"name": "Starner 20WP", "active": "Oxolinic Acid", "dose": "20g / bình 16 lít"},
            {"name": "Physan 20SL", "active": "Quaternary Ammonium Compounds", "dose": "15-20ml / bình 16 lít"},
            {"name": "Marthian 90SP", "active": "Streptomycin + Oxytetracycline", "dose": "1 gói 10g / bình 16 lít"}
        ]
    },

    # =========================================================================
    # 2. BỘ DỮ LIỆU PLANTDOC (27 LỚP THỰC ĐỊA)
    # =========================================================================
    "Apple Scab Leaf": {
        "name_en": "Apple Scab Leaf",
        "name_vi": "Cây Táo: Bệnh Ghẻ Lá (Apple Scab)",
        "short_name": "Táo: Bệnh Ghẻ Lá",
        "plant_type": "Cây Táo (Malus domestica)",
        "status_level": "danger",
        "status_text": "BỆNH NẤM GÂY HẠI LÁ TÁO",
        "badge_color": "#ef4444",
        "symptoms": ["Xuất hiện các đốm màu xanh ô liu đến nâu đen nhung trên mặt lá táo, làm lá biến dạng và rụng sớm."],
        "treatment": {"canh_tac": "Cào sạch lá rụng tiêu hủy nấm qua đông.", "dinh_duong": "Bón phân cân đối.", "phong_ngua": "Phun phòng ngừa vào mùa xuân khi chồi mới nhú."},
        "drugs": [{"name": "Score 250EC", "active": "Difenoconazole", "dose": "10ml / bình 16 lít"}]
    },
    "Apple leaf": {
        "name_en": "Apple leaf",
        "name_vi": "Cây Táo: Lá Khỏe Mạnh",
        "short_name": "Táo Khỏe Mạnh",
        "plant_type": "Cây Táo (Malus domestica)",
        "status_level": "safe",
        "status_text": "LÁ TÁO KHỎE MẠNH",
        "badge_color": "#10b981",
        "symptoms": ["Phiến lá màu xanh sáng, viền lá nhẵn nhụi hoặc răng cưa nhẹ, không có vết đốm nấm."],
        "treatment": {"canh_tac": "Duy trì bón phân hữu cơ và tưới tiêu hợp lý.", "dinh_duong": "Đầy đủ N-P-K vi lượng.", "phong_ngua": "Kiểm tra định kỳ sâu vẽ bùa."},
        "drugs": []
    },
    "Apple rust leaf": {
        "name_en": "Apple rust leaf",
        "name_vi": "Cây Táo: Bệnh Gỉ Sắt Lá Táo",
        "short_name": "Táo: Bệnh Gỉ Sắt",
        "plant_type": "Cây Táo (Malus domestica)",
        "status_level": "warning",
        "status_text": "BỆNH GỈ SẮT LÂY NHIỄM",
        "badge_color": "#f59e0b",
        "symptoms": ["Các đốm tròn màu vàng cam nổi gờ trên mặt trên phiến lá, mặt dưới mọc cụm bào tử gỉ."],
        "treatment": {"canh_tac": "Cách ly các loại cây ký chủ phụ quanh vườn táo.", "dinh_duong": "Bổ sung Kali.", "phong_ngua": "Phun thuốc trừ nấm phổ rộng."},
        "drugs": [{"name": "Anvil 5SC", "active": "Hexaconazole", "dose": "20ml / bình 16 lít"}]
    },
    "Bell_pepper leaf": {
        "name_en": "Bell_pepper leaf",
        "name_vi": "Cây Ớt Chuông: Lá Khỏe Mạnh",
        "short_name": "Ớt Chuông Khỏe Mạnh",
        "plant_type": "Cây Ớt Chuông (Capsicum annuum)",
        "status_level": "safe",
        "status_text": "LÁ ỚT CHUÔNG KHỎE MẠNH",
        "badge_color": "#10b981",
        "symptoms": ["Phiến lá xanh bóng, bản lá phẳng đều, không có biểu hiện xoăn ngọn hay đốm vi khuẩn."],
        "treatment": {"canh_tac": "Làm giàn chống đỡ, giữ ẩm đất.", "dinh_duong": "Bón thúc hữu cơ.", "phong_ngua": "Ngừa bọ trĩ chích hút."},
        "drugs": []
    },
    "Bell_pepper leaf spot": {
        "name_en": "Bell_pepper leaf spot",
        "name_vi": "Cây Ớt Chuông: Bệnh Đốm Lá Vi Khuẩn",
        "short_name": "Ớt Chuông: Đốm Lá",
        "plant_type": "Cây Ớt Chuông (Capsicum annuum)",
        "status_level": "danger",
        "status_text": "BỆNH ĐỐM LÁ VI KHUẨN",
        "badge_color": "#ef4444",
        "symptoms": ["Các đốm tròn nhỏ sũng nước màu nâu đen có quầng vàng xung quanh mép vết bệnh."],
        "treatment": {"canh_tac": "Không tưới phun mưa lúc nắng gắt.", "dinh_duong": "Tăng cường canxi.", "phong_ngua": "Phun thuốc gốc đồng ngừa vi khuẩn."},
        "drugs": [{"name": "Kasuran 47WP", "active": "Kasugamycin", "dose": "25g / bình 16 lít"}]
    },
    "Blueberry leaf": {
        "name_en": "Blueberry leaf",
        "name_vi": "Cây Việt Quất: Lá Khỏe Mạnh",
        "short_name": "Việt Quất Khỏe Mạnh",
        "plant_type": "Cây Việt Quất (Vaccinium)",
        "status_level": "safe",
        "status_text": "LÁ VIỆT QUẤT KHỎE MẠNH",
        "badge_color": "#10b981",
        "symptoms": ["Lá hình bầu dục, bóng, màu xanh lục đậm đồng nhất."],
        "treatment": {"canh_tac": "Duy trì đất có độ pH axit thích hợp (4.5 - 5.5).", "dinh_duong": "Bón phân hữu cơ vi sinh.", "phong_ngua": "Tưới tiêu hợp lý."},
        "drugs": []
    },
    "Cherry leaf": {
        "name_en": "Cherry leaf",
        "name_vi": "Cây Anh Đào: Lá Khỏe Mạnh",
        "short_name": "Anh Đào Khỏe Mạnh",
        "plant_type": "Cây Anh Đào (Prunus)",
        "status_level": "safe",
        "status_text": "LÁ ANH ĐÀO KHỎE MẠNH",
        "badge_color": "#10b981",
        "symptoms": ["Lá mũi mác xanh thẫm, gân lá rõ nét, không có vết cháy bìa lá."],
        "treatment": {"canh_tac": "Cắt tỉa cành hàng năm.", "dinh_duong": "Bón phân định kỳ.", "phong_ngua": "Theo dõi sâu đục thân."},
        "drugs": []
    },
    "Corn Gray leaf spot": {
        "name_en": "Corn Gray leaf spot",
        "name_vi": "Cây Ngô: Bệnh Đốm Xám Lá Ngô",
        "short_name": "Ngô: Bệnh Đốm Xám",
        "plant_type": "Cây Ngô / Bắp (Zea mays)",
        "status_level": "warning",
        "status_text": "BỆNH ĐỐM XÁM DỌC GÂN LÁ",
        "badge_color": "#f59e0b",
        "symptoms": ["Vệt bệnh hình chữ nhật dài màu nâu xám chạy song song giữa các gân lá ngô."],
        "treatment": {"canh_tac": "Luân canh cây họ đậu.", "dinh_duong": "Bón phân cân đối.", "phong_ngua": "Chọn giống kháng bệnh."},
        "drugs": [{"name": "Amistar Top 325SC", "active": "Azoxystrobin", "dose": "15ml / bình 16 lít"}]
    },
    "Corn leaf blight": {
        "name_en": "Corn leaf blight",
        "name_vi": "Cây Ngô: Bệnh Cháy Lá / Đốm Lớn",
        "short_name": "Ngô: Bệnh Cháy Lá",
        "plant_type": "Cây Ngô / Bắp (Zea mays)",
        "status_level": "danger",
        "status_text": "BỆNH CHÁY LÁ DIỆN RỘNG",
        "badge_color": "#ef4444",
        "symptoms": ["Các vệt dài hình thoi lớn màu xám xanh hoặc nâu bạc lan rộng làm khô toàn bộ phiến lá."],
        "treatment": {"canh_tac": "Cắt bỏ lá gốc bị bệnh nặng tiêu hủy.", "dinh_duong": "Tăng cường Kali.", "phong_ngua": "Phun khi phát hiện đốm đầu tiên."},
        "drugs": [{"name": "Tilt Super 300EC", "active": "Propiconazole", "dose": "10ml / bình 16 lít"}]
    },
    "Corn rust leaf": {
        "name_en": "Corn rust leaf",
        "name_vi": "Cây Ngô: Bệnh Gỉ Sắt Lá Ngô",
        "short_name": "Ngô: Bệnh Gỉ Sắt",
        "plant_type": "Cây Ngô / Bắp (Zea mays)",
        "status_level": "warning",
        "status_text": "BỆNH GỈ SẮT LÁ BẮP",
        "badge_color": "#f59e0b",
        "symptoms": ["Các nốt mụn nhỏ li ti màu nâu đỏ hoặc gỉ sắt nổi dày đặc ở cả hai mặt lá ngô."],
        "treatment": {"canh_tac": "Mật độ trồng thông thoáng.", "dinh_duong": "Hạn chế đạm muộn.", "phong_ngua": "Phun phòng khi thời tiết sương mù."},
        "drugs": [{"name": "Anvil 5SC", "active": "Hexaconazole", "dose": "20ml / bình 16 lít"}]
    },
    "Peach leaf": {
        "name_en": "Peach leaf",
        "name_vi": "Cây Đào: Lá Khỏe Mạnh",
        "short_name": "Đào Khỏe Mạnh",
        "plant_type": "Cây Đào (Prunus persica)",
        "status_level": "safe",
        "status_text": "LÁ ĐÀO KHỎE MẠNH",
        "badge_color": "#10b981",
        "symptoms": ["Phiến lá dài mũi mác xanh bóng, phẳng phiu, không bị xoăn phồng."],
        "treatment": {"canh_tac": "Tỉa cành tạo tán mở.", "dinh_duong": "Bón hữu cơ.", "phong_ngua": "Phòng bọ trĩ, rầy mềm."},
        "drugs": []
    },
    "Potato leaf early blight": {
        "name_en": "Potato leaf early blight",
        "name_vi": "Cây Khoai Tây: Bệnh Úa Sớm (Đốm Vòng)",
        "short_name": "Khoai Tây: Úa Sớm",
        "plant_type": "Cây Khoai Tây (Solanum tuberosum)",
        "status_level": "warning",
        "status_text": "BỆNH ĐỐM VÒNG ĐỒNG TÂM",
        "badge_color": "#f59e0b",
        "symptoms": ["Đốm màu nâu sẫm có các vòng tròn đồng tâm đặc trưng như hình bia bắn đạn."],
        "treatment": {"canh_tac": "Không trồng liền kề ruộng cà chua.", "dinh_duong": "Bón phân cân đối.", "phong_ngua": "Phun khi lá già bắt đầu đốm."},
        "drugs": [{"name": "Antracol 70WP", "active": "Propineb", "dose": "50g / bình 16 lít"}]
    },
    "Potato leaf late blight": {
        "name_en": "Potato leaf late blight",
        "name_vi": "Cây Khoai Tây: Bệnh Mốc Sương (Late Blight)",
        "short_name": "Khoai Tây: Mốc Sương",
        "plant_type": "Cây Khoai Tây (Solanum tuberosum)",
        "status_level": "danger",
        "status_text": "BỆNH MỐC SƯƠNG CỰC KỲ NGUY HIỂM",
        "badge_color": "#dc2626",
        "symptoms": ["Vết bệnh sũng nước màu nâu đen lan cực nhanh, mặt dưới có lớp nấm mốc trắng như bột."],
        "treatment": {"canh_tac": "Vun luống cao thoát nước tốt.", "dinh_duong": "Tăng lân và kali.", "phong_ngua": "Phun khẩn cấp thuốc nội hấp."},
        "drugs": [{"name": "Ridomil Gold 68WG", "active": "Metalaxyl-M + Mancozeb", "dose": "50g / bình 16 lít"}]
    },
    "Raspberry leaf": {
        "name_en": "Raspberry leaf",
        "name_vi": "Cây Mâm Xôi: Lá Khỏe Mạnh",
        "short_name": "Mâm Xôi Khỏe Mạnh",
        "plant_type": "Cây Mâm Xôi (Rubus)",
        "status_level": "safe",
        "status_text": "LÁ MÂM XÔI KHỎE MẠNH",
        "badge_color": "#10b981",
        "symptoms": ["Lá kép có răng cưa rõ ràng, xanh đậm, mặt dưới có lông mịn trắng."],
        "treatment": {"canh_tac": "Làm giàn nâng cành khỏi mặt đất.", "dinh_duong": "Bón hữu cơ định kỳ.", "phong_ngua": "Tưới gốc."},
        "drugs": []
    },
    "Soyabean leaf": {
        "name_en": "Soyabean leaf",
        "name_vi": "Cây Đậu Tương: Lá Khỏe Mạnh",
        "short_name": "Đậu Tương Khỏe Mạnh",
        "plant_type": "Cây Đậu Tương / Đậu Nành (Glycine max)",
        "status_level": "safe",
        "status_text": "LÁ ĐẬU TƯƠNG KHỎE MẠNH",
        "badge_color": "#10b981",
        "symptoms": ["Lá kép 3 lá chét xanh đều, không bị rỉ sắt hay sâu cuốn lá."],
        "treatment": {"canh_tac": "Luân canh mùa vụ lúa - đậu.", "dinh_duong": "Bón lân vi sinh kích rễ.", "phong_ngua": "Kiểm tra sâu khoang."},
        "drugs": []
    },
    "Squash Powdery mildew leaf": {
        "name_en": "Squash Powdery mildew leaf",
        "name_vi": "Cây Bí: Bệnh Phấn Trắng",
        "short_name": "Bí: Bệnh Phấn Trắng",
        "plant_type": "Cây Bí Ngô / Bí Đao (Cucurbita)",
        "status_level": "warning",
        "status_text": "BỆNH MỐC PHẤN TRẮNG PHIẾN LÁ",
        "badge_color": "#f59e0b",
        "symptoms": ["Lớp bột màu trắng xám bao phủ như rắc bột mì trên mặt phiến lá bí."],
        "treatment": {"canh_tac": "Cắt tỉa lá già sát đất thông thoáng.", "dinh_duong": "Giảm đạm.", "phong_ngua": "Phun thuốc đặc trị phấn trắng."},
        "drugs": [{"name": "Score 250EC", "active": "Difenoconazole", "dose": "10ml / bình 16 lít"}]
    },
    "Strawberry leaf": {
        "name_en": "Strawberry leaf",
        "name_vi": "Cây Dâu Tây: Lá Khỏe Mạnh",
        "short_name": "Dâu Tây Khỏe Mạnh",
        "plant_type": "Cây Dâu Tây (Fragaria)",
        "status_level": "safe",
        "status_text": "LÁ DÂU TÂY KHỎE MẠNH",
        "badge_color": "#10b981",
        "symptoms": ["Lá 3 lá chét viền răng cưa to tròn, xanh tươi, cuống lá cứng cáp."],
        "treatment": {"canh_tac": "Phủ bạt nilon giữ quả sạch.", "dinh_duong": "Tưới dinh dưỡng nhỏ giọt.", "phong_ngua": "Ngừa bọ trĩ, nhện đỏ."},
        "drugs": []
    },
    "Tomato Early blight leaf": {
        "name_en": "Tomato Early blight leaf",
        "name_vi": "Cây Cà Chua: Bệnh Úa Sớm (Đốm Vòng)",
        "short_name": "Cà Chua: Úa Sớm",
        "plant_type": "Cây Cà Chua (Solanum lycopersicum)",
        "status_level": "warning",
        "status_text": "BỆNH ĐỐM VÒNG ĐỒNG TÂM LÁ CÀ CHUA",
        "badge_color": "#f59e0b",
        "symptoms": ["Vết bệnh tròn màu nâu đen có vân vòng tròn đồng tâm, lá vàng rụng dần từ gốc lên ngọn."],
        "treatment": {"canh_tac": "Ngắt bỏ lá gốc bị bệnh chôn tiêu hủy.", "dinh_duong": "Bón phân cân đối.", "phong_ngua": "Phun phòng ngừa mùa mưa."},
        "drugs": [{"name": "Score 250EC", "active": "Difenoconazole", "dose": "10-15ml / bình 16 lít"}]
    },
    "Tomato Septoria leaf spot": {
        "name_en": "Tomato Septoria leaf spot",
        "name_vi": "Cây Cà Chua: Bệnh Đốm Lá Septoria",
        "short_name": "Cà Chua: Đốm Septoria",
        "plant_type": "Cây Cà Chua (Solanum lycopersicum)",
        "status_level": "warning",
        "status_text": "BỆNH ĐỐM LÁ CHẤM NHỎ SEPTORIA",
        "badge_color": "#f59e0b",
        "symptoms": ["Hàng loạt đốm tròn nhỏ li ti (1-3mm) tâm xám viền nâu sẫm dày đặc trên phiến lá cà chua."],
        "treatment": {"canh_tac": "Không tưới phun lên tán lá.", "dinh_duong": "Tăng kali hữu cơ.", "phong_ngua": "Phun luân phiên thuốc nấm."},
        "drugs": [{"name": "Antracol 70WP", "active": "Propineb", "dose": "50g / bình 16 lít"}]
    },
    "Tomato leaf": {
        "name_en": "Tomato leaf",
        "name_vi": "Cây Cà Chua: Lá Khỏe Mạnh",
        "short_name": "Cà Chua Khỏe Mạnh",
        "plant_type": "Cây Cà Chua (Solanum lycopersicum)",
        "status_level": "safe",
        "status_text": "LÁ CÀ CHUA KHỎE MẠNH",
        "badge_color": "#10b981",
        "symptoms": ["Lá kép xẻ thùy màu xanh tươi, phiến lá phẳng phiu, không có chấm đốm hay quăn queo."],
        "treatment": {"canh_tac": "Buộc dây định hướng cành leo giàn.", "dinh_duong": "Tưới nước đều đặn.", "phong_ngua": "Kiểm tra sâu đục quả."},
        "drugs": []
    },
    "Tomato leaf bacterial spot": {
        "name_en": "Tomato leaf bacterial spot",
        "name_vi": "Cây Cà Chua: Bệnh Đốm Vi Khuẩn",
        "short_name": "Cà Chua: Đốm Vi Khuẩn",
        "plant_type": "Cây Cà Chua (Solanum lycopersicum)",
        "status_level": "danger",
        "status_text": "BỆNH ĐỐM DO VI KHUẨN TẤN CÔNG",
        "badge_color": "#ef4444",
        "symptoms": ["Đốm sũng nước màu nâu đen, mép có quầng vàng nhờn bóng, làm rách rách phiến lá."],
        "treatment": {"canh_tac": "Nhổ bỏ cây bệnh nặng để tránh lây qua gió mưa.", "dinh_duong": "Giảm đạm ngay.", "phong_ngua": "Phun thuốc kháng khuẩn gốc đồng."},
        "drugs": [{"name": "Kasuran 47WP", "active": "Kasugamycin + Đồng", "dose": "30g / bình 16 lít"}]
    },
    "Tomato leaf late blight": {
        "name_en": "Tomato leaf late blight",
        "name_vi": "Cây Cà Chua: Bệnh Mốc Sương (Sương Mai)",
        "short_name": "Cà Chua: Mốc Sương",
        "plant_type": "Cây Cà Chua (Solanum lycopersicum)",
        "status_level": "danger",
        "status_text": "BỆNH MỐC SƯƠNG GÂY THỐI LÁ RỤNG CÀY",
        "badge_color": "#dc2626",
        "symptoms": ["Vết bệnh ủng nước màu xanh xám rồi chuyển nâu đen, nấm mốc trắng ở mặt dưới lá."],
        "treatment": {"canh_tac": "Cắt tỉa lá gốc, tưới rãnh không tưới ngọn.", "dinh_duong": "Tăng kali.", "phong_ngua": "Phun ngay khi có sương muối kéo dài."},
        "drugs": [{"name": "Ridomil Gold 68WG", "active": "Metalaxyl-M + Mancozeb", "dose": "50g / bình 16 lít"}]
    },
    "Tomato leaf mosaic virus": {
        "name_en": "Tomato leaf mosaic virus",
        "name_vi": "Cây Cà Chua: Bệnh Virus Khảm Lá (ToMV)",
        "short_name": "Cà Chua: Virus Khảm Lá",
        "plant_type": "Cây Cà Chua (Solanum lycopersicum)",
        "status_level": "danger",
        "status_text": "BỆNH VIRUS NGUY HIỂM - KHÔNG CÓ THUỐC ĐẶC TRỊ",
        "badge_color": "#b91c1c",
        "symptoms": ["Lá bị loang lổ xen kẽ các vệt xanh đậm và vàng nhạt, phiến lá nhăn nheo biến dạng."],
        "treatment": {"canh_tac": "Nhổ bỏ ngay cây bị virus đem đốt để tránh bọ trĩ rầy mềm chích hút lây bệnh.", "dinh_duong": "Tăng sức đề kháng.", "phong_ngua": "Phun diệt côn trùng truyền bệnh."},
        "drugs": [{"name": "Admire 050EC", "active": "Imidacloprid (Diệt rầy truyền virus)", "dose": "10ml / bình 16 lít"}]
    },
    "Tomato leaf yellow virus": {
        "name_en": "Tomato leaf yellow virus",
        "name_vi": "Cây Cà Chua: Bệnh Virus Xoăn Vàng Lá (TYLCV)",
        "short_name": "Cà Chua: Xoăn Vàng Lá",
        "plant_type": "Cây Cà Chua (Solanum lycopersicum)",
        "status_level": "danger",
        "status_text": "BỆNH VIRUS XOĂN LÁ CÀ CHUA",
        "badge_color": "#b91c1c",
        "symptoms": ["Lá non bị co quắp, cong queo lòng thuyền, mép lá và ngọn chuyển sang màu vàng tươi."],
        "treatment": {"canh_tac": "Tiêu hủy cây bệnh, vệ sinh nhà màng nhà lưới.", "dinh_duong": "Tăng vi lượng.", "phong_ngua": "Diệt bọ phấn trắng triệt để."},
        "drugs": [{"name": "Confidor 100SL", "active": "Imidacloprid", "dose": "10-15ml / bình 16 lít"}]
    },
    "Tomato mold leaf": {
        "name_en": "Tomato mold leaf",
        "name_vi": "Cây Cà Chua: Bệnh Mốc Lá (Leaf Mold)",
        "short_name": "Cà Chua: Bệnh Mốc Lá",
        "plant_type": "Cây Cà Chua (Solanum lycopersicum)",
        "status_level": "warning",
        "status_text": "BỆNH MỐC LÁ ĐỘ ẨM CAO",
        "badge_color": "#f59e0b",
        "symptoms": ["Mặt trên lá có đốm màu vàng nhạt, mặt dưới có lớp nấm mịn màu xám nhung ô liu."],
        "treatment": {"canh_tac": "Hạ thấp độ ẩm trong nhà lưới/ruộng, thông gió tốt.", "dinh_duong": "Bón phân cân đối.", "phong_ngua": "Phun khi phát hiện đốm đầu tiên."},
        "drugs": [{"name": "Score 250EC", "active": "Difenoconazole", "dose": "10ml / bình 16 lít"}]
    },
    "grape leaf": {
        "name_en": "grape leaf",
        "name_vi": "Cây Nho: Lá Khỏe Mạnh",
        "short_name": "Nho Khỏe Mạnh",
        "plant_type": "Cây Nho (Vitis vinifera)",
        "status_level": "safe",
        "status_text": "LÁ NHO KHỎE MẠNH",
        "badge_color": "#10b981",
        "symptoms": ["Lá hình tim xẻ thùy xanh mướt, phiến lá phẳng bóng, không có đốm cháy."],
        "treatment": {"canh_tac": "Buộc cành tỉa chồi nách hợp lý.", "dinh_duong": "Tưới tiêu đủ ẩm.", "phong_ngua": "Phòng bọ trĩ, rệp sáp."},
        "drugs": []
    },
    "grape leaf black rot": {
        "name_en": "grape leaf black rot",
        "name_vi": "Cây Nho: Bệnh Thối Đen (Black Rot)",
        "short_name": "Nho: Bệnh Thối Đen",
        "plant_type": "Cây Nho (Vitis vinifera)",
        "status_level": "danger",
        "status_text": "BỆNH THỐI ĐEN NGUY HIỂM TRÊN NHO",
        "badge_color": "#ef4444",
        "symptoms": ["Các đốm tròn màu nâu đỏ có viền đen rõ rệt, trên vết bệnh mọc các chấm đen li ti."],
        "treatment": {"canh_tac": "Cắt tỉa thông thoáng giàn nho, thu gom lá bệnh rụng đem đốt.", "dinh_duong": "Tăng kali.", "phong_ngua": "Phun thuốc định kỳ mùa mưa."},
        "drugs": [{"name": "Amistar Top 325SC", "active": "Azoxystrobin", "dose": "15ml / bình 16 lít"}]
    }
}

def get_disease_info(class_name: str) -> dict:
    """Tra cứu thông tin chi tiết cho bất kỳ class nào trong 33 lớp"""
    if class_name in KNOWLEDGE_BASE:
        return KNOWLEDGE_BASE[class_name]
    
    # Mặc định an toàn nếu class_name chưa đăng ký
    return {
        "name_en": class_name,
        "name_vi": f"Nhận Diện: {class_name}",
        "short_name": class_name,
        "plant_type": "Cây trồng thực địa",
        "status_level": "info",
        "status_text": "KẾT QUẢ CHẨN ĐOÁN MÔ HÌNH",
        "badge_color": "#3b82f6",
        "symptoms": ["Dữ liệu nhận dạng từ bộ mô hình học máy ResNet18."],
        "treatment": {
            "canh_tac": "Theo dõi tình trạng cây trồng thường xuyên.",
            "dinh_duong": "Bón phân cân đối N-P-K.",
            "phong_ngua": "Khảo sát và phòng ngừa sâu bệnh định kỳ."
        },
        "drugs": []
    }
