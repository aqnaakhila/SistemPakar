from forward_reasoning.kategory import *

def infer(data):
    data = kategorikan_input(data)
    inferred = {}

    # Layanan Teknis
    if data['Stabilitas Jaringan'] == 'Baik' and data['Kapasitas Bandwidth'] in ['Besar', 'Sedang']:
        inferred['Layanan Teknis'] = 'Tidak perlu upgrade kualitas'
    else:
        inferred['Layanan Teknis'] = 'Upgrade kualitas'

    # Strategi Bisnis
    if data['Pelayanan'] == 'Baik':
        inferred['Strategi Bisnis'] = 'Tidak perlu perbaikan'
    else:
        inferred['Strategi Bisnis'] = 'Perlu perbaikan'

    # Kepuasan Pelanggan
    if data['Rating Kategori'] in ['Bagus', 'Normal'] and data['Kualitas Layanan'] == 'Bagus':
        inferred['Kepuasan Pelanggan'] = 'Pelanggan puas'
    else:
        inferred['Kepuasan Pelanggan'] = 'Pelanggan tidak puas'

    # Kesimpulan ISP
    lt = inferred['Layanan Teknis']
    sb = inferred['Strategi Bisnis']
    kp = data['Kepatuhan Regulasi']
    kpgn = inferred['Kepuasan Pelanggan']

    result = "Tidak dapat disimpulkan"
    explanation = []  # simpan penjelasan

    # Tambahkan logika explain di tiap rule
    if lt == 'Upgrade kualitas' and sb == 'Tidak perlu perbaikan' and kp == 'Memenuhi aturan' and kpgn == 'Pelanggan puas':
        result = 'ISP Berkualitas Baik'
        explanation.append("Rule 1: Semua kondisi terpenuhi → ISP Berkualitas Baik")
    elif lt == 'Upgrade kualitas' and sb == 'Tidak perlu perbaikan' and kp == 'Memenuhi aturan' and kpgn == 'Pelanggan tidak puas':
        result = 'ISP Bermasalah'
        explanation.append("Rule 2: Pelanggan tidak puas → ISP Bermasalah")
    elif lt == 'Upgrade kualitas' and sb == 'Perlu perbaikan' and kpgn == 'Pelanggan puas':
        result = 'ISP Perlu Peningkatan'
        explanation.append("Rule 3: Perlu perbaikan strategi + pelanggan puas → ISP Perlu Peningkatan")
    elif lt == 'Upgrade kualitas' and sb == 'Perlu perbaikan' and kpgn == 'Pelanggan tidak puas':
        result = 'ISP Bermasalah'
        explanation.append("Rule 4: Semua buruk → ISP Bermasalah")
    elif lt == 'Tidak perlu upgrade kualitas' and sb == 'Tidak perlu perbaikan' and kpgn == 'Pelanggan puas':
        result = 'ISP Berkualitas Baik'
        explanation.append("Rule 6: Semua baik → ISP Berkualitas Baik")
    elif lt == 'Tidak perlu upgrade kualitas' and sb == 'Tidak perlu perbaikan' and kpgn == 'Pelanggan tidak puas':
        result = 'ISP Perlu Peningkatan'
        explanation.append("Rule 7: Tidak puas → ISP Perlu Peningkatan")
    elif lt == 'Tidak perlu upgrade kualitas' and sb == 'Perlu perbaikan' and kp == 'Memenuhi aturan' and kpgn == 'Pelanggan puas':
        result = 'ISP Berkualitas Baik'
        explanation.append("Rule 8: Walau strategi perlu perbaikan, tapi aturan & pelanggan puas → ISP Baik")
    elif lt == 'Tidak perlu upgrade kualitas' and sb == 'Perlu perbaikan' and kpgn == 'Pelanggan puas':
        result = 'ISP Perlu Perbaikan'
        explanation.append("Rule 9/10: Strategi perlu perbaikan → ISP Perlu Perbaikan")
    elif lt == 'Tidak perlu upgrade kualitas' and sb == 'Perlu perbaikan' and kp == 'Tidak memenuhi aturan' and kpgn == 'Pelanggan tidak puas':
        result = 'ISP Bermasalah'
        explanation.append("Rule 11: Semua buruk → ISP Bermasalah")
    else:
        explanation.append("Tidak ada rule yang cocok sepenuhnya dengan kondisi saat ini.")

    return result, inferred, explanation
