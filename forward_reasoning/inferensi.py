from forward_reasoning.kategory import kategorikan_input

def infer(data):
    data = kategorikan_input(data)
    inferred = {}

    # Aturan 12–14 - Layanan Teknis
    if data['Stabilitas Jaringan'] == 'Baik' and data['Kapasitas Bandwidth'] in ['Besar', 'Sedang']:
        inferred['Layanan Teknis'] = 'Tidak perlu upgrade kualitas'
    else:
        inferred['Layanan Teknis'] = 'perlu Upgrade kualitas'

    # Aturan 15–16 - Strategi Bisnis
    if data['Pelayanan'] == 'Baik':
        inferred['Strategi Bisnis'] = 'Tidak perlu perbaikan'
    else:
        inferred['Strategi Bisnis'] = 'Perlu perbaikan'

    # Aturan 17–19 - Kepuasan Pelanggan
    if data['Kualitas Layanan'] == 'Bagus':
        inferred['Kepuasan Pelanggan'] = 'Pelanggan puas'
    else:
        inferred['Kepuasan Pelanggan'] = 'Pelanggan tidak puas'

    # Kesimpulan ISP - Aturan 1–15
    lt = inferred['Layanan Teknis']
    sb = inferred['Strategi Bisnis']
    kr = data['Kepatuhan Regulasi']
    kp = inferred['Kepuasan Pelanggan']

    result = "Tidak dapat disimpulkan"
    explanation = []

    # Aturan 1
    if lt == 'perlu Upgrade kualitas' and sb == 'Tidak perlu perbaikan' and kr == 'Memenuhi aturan' and kp == 'Pelanggan puas':
        result = 'ISP Perlu Peningkatan'
        explanation.append("Rule 7: Semua kondisi baik tapi layanan teknis perlu upgrade → ISP Perlu peningkatan")

    # Aturan 2
    elif lt == 'perlu Upgrade kualitas' and sb == 'Tidak perlu perbaikan' and kr == 'Memenuhi aturan' and kp == 'Pelanggan tidak puas':
        result = 'ISP Bermasalah'
        explanation.append("Rule 8: Pelanggan tidak puas → ISP Bermasalah")

    # Aturan 3
    elif lt == 'perlu Upgrade kualitas' and sb == 'Perlu perbaikan' and kp == 'Pelanggan puas':
        result = 'ISP Perlu Peningkatan'
        explanation.append("Rule 9: Strategi perlu perbaikan tapi pelanggan puas → ISP Perlu Peningkatan")

    # Aturan 4
    elif lt == 'perlu Upgrade kualitas' and sb == 'Perlu perbaikan' and kp == 'Pelanggan tidak puas':
        result = 'ISP Bermasalah'
        explanation.append("Rule 10: Semua buruk → ISP Bermasalah")

    # Aturan 5
    elif lt == 'perlu Upgrade kualitas' and sb == 'Perlu perbaikan' and kr == 'Tidak memenuhi aturan':
        result = 'ISP Bermasalah'
        explanation.append("Rule 11: Upgrade + strategi buruk + tidak memenuhi aturan → ISP Bermasalah")

    # Aturan 6
    elif lt == 'Tidak perlu upgrade kualitas' and sb == 'Tidak perlu perbaikan' and kp == 'Pelanggan puas':
        result = 'ISP Berkualitas Baik'
        explanation.append("Rule 12: Semua baik → ISP Berkualitas Baik")

    # Aturan 7
    elif lt == 'Tidak perlu upgrade kualitas' and sb == 'Tidak perlu perbaikan' and kp == 'Pelanggan tidak puas':
        result = 'ISP Perlu Peningkatan'
        explanation.append("Rule 13: Pelanggan tidak puas → ISP Perlu Peningkatan")

    # Aturan 8
    elif lt == 'Tidak perlu upgrade kualitas' and sb == 'Perlu perbaikan' and kr == 'Memenuhi aturan' and kp == 'Pelanggan puas':
        result = 'ISP Berkualitas Baik'
        explanation.append("Rule 14: Hanya strategi yang lemah → ISP Berkualitas Baik")

    # Aturan 9
    elif lt == 'Tidak perlu upgrade kualitas' and sb == 'Perlu perbaikan' and kr == 'Memenuhi aturan' and kp == 'Pelanggan puas':
        result = 'ISP Perlu Peningkatan'
        explanation.append("Rule 15: Strategi lemah meski lainnya baik → ISP Perlu Peningkatan")

    # Aturan 10
    elif lt == 'Tidak perlu upgrade kualitas' and sb == 'Perlu perbaikan' and kr == 'Tidak memenuhi aturan' and kp == 'Pelanggan puas':
        result = 'ISP Perlu Peningkatan'
        explanation.append("Rule 16: Beberapa komponen bermasalah → ISP Perlu Peningkatan")

    # Aturan 11
    elif lt == 'Tidak perlu upgrade kualitas' and sb == 'Perlu perbaikan' and kr == 'Tidak memenuhi aturan' and kp == 'Pelanggan tidak puas':
        result = 'ISP Bermasalah'
        explanation.append("Rule 17: Semua komponen bermasalah → ISP Bermasalah")

    # Rule 13
    elif lt == 'Tidak perlu upgrade kualitas' and sb == 'Tidak perlu perbaikan' and kr == 'Tidak memenuhi aturan' and kp == 'Pelanggan tidak puas':
        result = 'ISP Perlu Peningkatan'
        explanation.append("Rule 18: Regulasi dan pelanggan buruk meski layanan bagus → ISP Perlu Peningkatan")

    # Rule 14
    elif lt == 'perlu Upgrade kualitas' and sb == 'Tidak perlu perbaikan' and kr == 'Tidak memenuhi aturan' and kp == 'Pelanggan puas':
        result = 'ISP Perlu Peningkatan'
        explanation.append("Rule 19: Regulasi dan teknis lemah meski pelanggan puas → ISP Perlu Peningkatan")

    # Rule 15
    elif lt == 'Tidak perlu upgrade kualitas' and sb == 'Perlu perbaikan' and kr == 'Memenuhi aturan' and kp == 'Pelanggan tidak puas':
        result = 'ISP Perlu Peningkatan'
        explanation.append("Rule 20: Strategi buruk dan pelanggan tidak puas → ISP Perlu Peningkatan")

    else:
        explanation.append("Tidak ada rule yang cocok sepenuhnya dengan kondisi saat ini.")

    return result, inferred, explanation