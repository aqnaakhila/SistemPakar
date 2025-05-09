from forward_reasoning.kategory import kategorikan_input

def infer(data):
    # Kategorisasi awal input
    data = kategorikan_input(data)
    inferred = {}

    # Aturan 12, 13, 14 - Layanan Teknis
    if data['Stabilitas Jaringan'] == 'Baik' and data['Kapasitas Bandwidth'] in ['Besar', 'Sedang']:
        inferred['Layanan Teknis'] = 'Tidak perlu upgrade kualitas'
    else:
        inferred['Layanan Teknis'] = 'perlu Upgrade kualitas'

    # Aturan 15, 16 - Strategi Bisnis
    if data['Pelayanan'] == 'Baik':
        inferred['Strategi Bisnis'] = 'Tidak perlu perbaikan'
    else:
        inferred['Strategi Bisnis'] = 'Perlu perbaikan'

    # Aturan 17, 18, 19 - Kepuasan Pelanggan
    if data['Rating Kategori'] in ['Bagus', 'Normal'] and data['Kualitas Layanan'] == 'Bagus':
        inferred['Kepuasan Pelanggan'] = 'Pelanggan puas'
    else:
        inferred['Kepuasan Pelanggan'] = 'Pelanggan tidak puas'

    # Kesimpulan ISP - Aturan 1-11
    layananteknis = inferred['Layanan Teknis']
    strategibisnis = inferred['Strategi Bisnis']
    kepatuhanregulasi = data['Kepatuhan Regulasi']
    kepuasanpelanggan = inferred['Kepuasan Pelanggan']

    result = "Tidak dapat disimpulkan"
    explanation = []

    if layananteknis == 'perlu Upgrade kualitas' and strategibisnis == 'Tidak perlu perbaikan' and kepatuhanregulasi == 'Memenuhi aturan' and kepuasanpelanggan == 'Pelanggan puas':
        result = 'ISP Perlu Peningkatan'
        explanation.append("Rule 1: Semua kondisi baik tapi layanan teknis perlu upgrade kualitas → ISP Perlu peningkatan")
    elif layananteknis == 'perlu Upgrade kualitas' and strategibisnis == 'Tidak perlu perbaikan' and kepatuhanregulasi == 'Memenuhi aturan' and kepuasanpelanggan == 'Pelanggan tidak puas':
        result = 'ISP Bermasalah'
        explanation.append("Rule 2: Pelanggan tidak puas → ISP Bermasalah")
    elif layananteknis == 'perlu Upgrade kualitas' and strategibisnis == 'Perlu perbaikan' and kepuasanpelanggan == 'Pelanggan puas':
        result = 'ISP Perlu Peningkatan'
        explanation.append("Rule 3: Strategi perlu perbaikan tapi pelanggan puas → ISP Perlu Peningkatan")
    elif layananteknis == 'perlu Upgrade kualitas' and strategibisnis == 'Perlu perbaikan' and kepuasanpelanggan == 'Pelanggan tidak puas':
        result = 'ISP Bermasalah'
        explanation.append("Rule 4: Semua buruk → ISP Bermasalah")
    elif layananteknis == 'perlu Upgrade kualitas' and strategibisnis == 'Perlu perbaikan' and kepatuhanregulasi == 'Tidak memenuhi aturan':
        result = 'ISP Bermasalah'
        explanation.append("Rule 5: Upgrade + strategi buruk + tidak memenuhi aturan → ISP Bermasalah")
    elif layananteknis == 'Tidak perlu upgrade kualitas' and strategibisnis == 'Tidak perlu perbaikan' and kepuasanpelanggan == 'Pelanggan puas':
        result = 'ISP Berkualitas Baik'
        explanation.append("Rule 6: Semua baik → ISP Berkualitas Baik")
    elif layananteknis == 'Tidak perlu upgrade kualitas' and strategibisnis == 'Tidak perlu perbaikan' and kepuasanpelanggan == 'Pelanggan tidak puas':
        result = 'ISP Perlu Peningkatan'
        explanation.append("Rule 7: Pelanggan tidak puas → ISP Perlu Peningkatan")
    elif layananteknis == 'Tidak perlu upgrade kualitas' and strategibisnis == 'Perlu perbaikan' and kepatuhanregulasi == 'Memenuhi aturan' and kepuasanpelanggan == 'Pelanggan puas':
        result = 'ISP Berkualitas Baik'
        explanation.append("Rule 8: Hanya strategi yang lemah → ISP Berkualitas Baik")
    elif layananteknis == 'Tidak perlu upgrade kualitas' and strategibisnis == 'Perlu perbaikan' and kepatuhanregulasi == 'Memenuhi aturan' and kepuasanpelanggan == 'Pelanggan puas':
        result = 'ISP Perlu Perbaikan'
        explanation.append("Rule 9: Strategi lemah meski lainnya baik → ISP Perlu Perbaikan")
    elif layananteknis == 'Tidak perlu upgrade kualitas' and strategibisnis == 'Perlu perbaikan' and kepatuhanregulasi == 'Tidak memenuhi aturan' and kepuasanpelanggan == 'Pelanggan puas':
        result = 'ISP Perlu Perbaikan'
        explanation.append("Rule 10: Beberapa komponen bermasalah → ISP Perlu Perbaikan")
    elif layananteknis == 'Tidak perlu upgrade kualitas' and strategibisnis == 'Perlu perbaikan' and kepatuhanregulasi == 'Tidak memenuhi aturan' and kepuasanpelanggan == 'Pelanggan tidak puas':
        result = 'ISP Bermasalah'
        explanation.append("Rule 11: Semua buruk → ISP Bermasalah")
    
    else:
        explanation.append("Tidak ada rule yang cocok sepenuhnya dengan kondisi saat ini.")

    return result, inferred, explanation
