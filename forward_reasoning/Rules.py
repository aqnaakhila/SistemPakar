rules = [
    # Rule 1
    {"if": [("Stabilitas Jaringan", "Baik"), ("Kapasitas Bandwidth", "Besar")], "then": "Layanan Teknis = Tidak perlu upgrade kualitas", "cf": 0.8},
    {"if": [("Stabilitas Jaringan", "Baik"), ("Kapasitas Bandwidth", "Sedang")], "then": "Layanan Teknis = Tidak perlu upgrade kualitas", "cf": 0.8},
    {"if": [("Stabilitas Jaringan", "Baik"), ("Kapasitas Bandwidth", "Rendah")], "then": "Layanan Teknis = Tidak perlu upgrade kualitas", "cf": 0.8},

    # Rule 2
    {"if": [("Stabilitas Jaringan", "Buruk"), ("Kapasitas Bandwidth", "Besar")], "then": "Layanan Teknis = Perlu upgrade kualitas", "cf": 0.7},
    {"if": [("Stabilitas Jaringan", "Buruk"), ("Kapasitas Bandwidth", "Sedang")], "then": "Layanan Teknis = Perlu upgrade kualitas", "cf": 0.7},
    {"if": [("Stabilitas Jaringan", "Buruk"), ("Kapasitas Bandwidth", "Rendah")], "then": "Layanan Teknis = Perlu upgrade kualitas", "cf": 0.7},

    # Rule 3
    {"if": [("Harga Kategori", "Murah"), ("Pelayanan", "Baik")], "then": "Strategi Bisnis = Tidak perlu perbaikan", "cf": 0.9},
    {"if": [("Harga Kategori", "Standar"), ("Pelayanan", "Baik")], "then": "Strategi Bisnis = Tidak perlu perbaikan", "cf": 0.9},
    {"if": [("Harga Kategori", "Mahal"), ("Pelayanan", "Baik")], "then": "Strategi Bisnis = Tidak perlu perbaikan", "cf": 0.9},

    # Rule 4
    {"if": [("Harga Kategori", "Murah"), ("Pelayanan", "Buruk")], "then": "Strategi Bisnis = Perlu perbaikan", "cf": 0.8},
    {"if": [("Harga Kategori", "Standar"), ("Pelayanan", "Buruk")], "then": "Strategi Bisnis = Perlu perbaikan", "cf": 0.8},
    {"if": [("Harga Kategori", "Mahal"), ("Pelayanan", "Buruk")], "then": "Strategi Bisnis = Perlu perbaikan", "cf": 0.8},

    # Rule 5
    {"if": [("Rating Kategori", "Bagus"), ("Kualitas Layanan", "Bagus")], "then": "Kepuasan Pelanggan = Pelanggan puas", "cf": 0.85},
    {"if": [("Rating Kategori", "Normal"), ("Kualitas Layanan", "Bagus")], "then": "Kepuasan Pelanggan = Pelanggan puas", "cf": 0.85},

    # Rule 6
    {"if": [("Rating Kategori", "Buruk"), ("Kualitas Layanan", "Bagus")], "then": "Kepuasan Pelanggan = Pelanggan tidak puas", "cf": 0.7},

    # Rule 7
    {"if": [("Rating Kategori", "Bagus"), ("Kualitas Layanan", "Buruk")], "then": "Kepuasan Pelanggan = Pelanggan tidak puas", "cf": 0.9},
    {"if": [("Rating Kategori", "Normal"), ("Kualitas Layanan", "Buruk")], "then": "Kepuasan Pelanggan = Pelanggan tidak puas", "cf": 0.9},
    {"if": [("Rating Kategori", "Buruk"), ("Kualitas Layanan", "Buruk")], "then": "Kepuasan Pelanggan = Pelanggan tidak puas", "cf": 0.9},

    # Rules 8–21 (tidak perlu dipecah karena tidak mengandung OR)
    {"if": [("Layanan Teknis", "Perlu upgrade kualitas"), ("Strategi Bisnis", "Tidak perlu perbaikan"), ("Kepatuhan Regulasi", "Memenuhi aturan"), ("Kepuasan Pelanggan", "Pelanggan puas")], "then": "ISP Local = ISP Perlu Peningkatan", "cf": 0.75},
    {"if": [("Layanan Teknis", "Perlu upgrade kualitas"), ("Strategi Bisnis", "Tidak perlu perbaikan"), ("Kepatuhan Regulasi", "Memenuhi aturan"), ("Kepuasan Pelanggan", "Pelanggan tidak puas")], "then": "ISP Local = ISP Bermasalah", "cf": 0.8},
    {"if": [("Layanan Teknis", "Perlu upgrade kualitas"), ("Strategi Bisnis", "Perlu perbaikan"), ("Kepuasan Pelanggan", "Pelanggan puas")], "then": "ISP Local = ISP Perlu Peningkatan", "cf": 0.7},
    {"if": [("Layanan Teknis", "Perlu upgrade kualitas"), ("Strategi Bisnis", "Perlu perbaikan"), ("Kepuasan Pelanggan", "Pelanggan tidak puas")], "then": "ISP Local = ISP Bermasalah", "cf": 0.8},
    {"if": [("Layanan Teknis", "Perlu upgrade kualitas"), ("Strategi Bisnis", "Perlu perbaikan"), ("Kepatuhan Regulasi", "Tidak memenuhi aturan")], "then": "ISP Local = ISP Bermasalah", "cf": 0.75},
    {"if": [("Layanan Teknis", "Tidak perlu upgrade kualitas"), ("Strategi Bisnis", "Tidak perlu perbaikan"), ("Kepatuhan Regulasi", "Memenuhi aturan"), ("Kepuasan Pelanggan", "Pelanggan puas")], "then": "ISP Local = ISP Berkualitas Baik", "cf": 0.85},
    {"if": [("Layanan Teknis", "Tidak perlu upgrade kualitas"), ("Strategi Bisnis", "Tidak perlu perbaikan"), ("Kepatuhan Regulasi", "Memenuhi aturan"), ("Kepuasan Pelanggan", "Pelanggan tidak puas")], "then": "ISP Local = ISP Perlu Peningkatan", "cf": 0.7},
    {"if": [("Layanan Teknis", "Tidak perlu upgrade kualitas"), ("Strategi Bisnis", "Perlu perbaikan"), ("Kepatuhan Regulasi", "Memenuhi aturan"), ("Kepuasan Pelanggan", "Pelanggan puas")], "then": "ISP Local = ISP Berkualitas Baik", "cf": 0.8},
    {"if": [("Layanan Teknis", "Perlu upgrade kualitas"), ("Strategi Bisnis", "Perlu perbaikan"), ("Kepatuhan Regulasi", "Memenuhi aturan"), ("Kepuasan Pelanggan", "Pelanggan puas")], "then": "ISP Local = ISP Perlu Peningkatan", "cf": 0.75},
    {"if": [("Layanan Teknis", "Tidak perlu upgrade kualitas"), ("Strategi Bisnis", "Perlu perbaikan"), ("Kepatuhan Regulasi", "Tidak memenuhi aturan"), ("Kepuasan Pelanggan", "Pelanggan puas")], "then": "ISP Local = ISP Perlu Peningkatan", "cf": 0.7},
    {"if": [("Layanan Teknis", "Tidak perlu upgrade kualitas"), ("Strategi Bisnis", "Perlu perbaikan"), ("Kepatuhan Regulasi", "Tidak memenuhi aturan"), ("Kepuasan Pelanggan", "Pelanggan tidak puas")], "then": "ISP Local = ISP Bermasalah", "cf": 0.8},
    {"if": [("Layanan Teknis", "Tidak perlu upgrade kualitas"), ("Strategi Bisnis", "Tidak perlu perbaikan"), ("Kepatuhan Regulasi", "Tidak memenuhi aturan"), ("Kepuasan Pelanggan", "Pelanggan tidak puas")], "then": "ISP Local = ISP Perlu Peningkatan", "cf": 0.7},
    {"if": [("Layanan Teknis", "Tidak perlu upgrade kualitas"), ("Strategi Bisnis", "Perlu perbaikan"), ("Kepatuhan Regulasi", "Memenuhi aturan"), ("Kepuasan Pelanggan", "Pelanggan tidak puas")], "then": "ISP Local = ISP Perlu Peningkatan", "cf": 0.75},
    {"if": [("Layanan Teknis", "Perlu upgrade kualitas"), ("Strategi Bisnis", "Tidak perlu perbaikan"), ("Kepatuhan Regulasi", "Tidak memenuhi aturan"), ("Kepuasan Pelanggan", "Pelanggan puas")], "then": "ISP Local = ISP Perlu Peningkatan", "cf": 0.8}
]
