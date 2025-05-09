def kategorikan_input(data):
    result = {}

    # Stabilitas Jaringan: RTO
    rto = int(data['RTO'])
    result['Stabilitas Jaringan'] = 'Baik' if rto <= 2 else 'Buruk'

    # Kapasitas Bandwidth (Mbps)
    bw = float(data['Bandwidth'])
    if bw > 50:
        result['Kapasitas Bandwidth'] = 'Besar'
    elif bw >= 20:
        result['Kapasitas Bandwidth'] = 'Sedang'
    else:
        result['Kapasitas Bandwidth'] = 'Rendah'

    # Harga (Rp)
    harga = int(data['Harga'])
    if harga < 100000:
        result['Harga Kategori'] = 'Murah'
    elif harga <= 300000:
        result['Harga Kategori'] = 'Standar'
    else:
        result['Harga Kategori'] = 'Mahal'

    # Rating (0–10)
    rating = float(data['Rating'])
    if rating >= 8:
        result['Rating Kategori'] = 'Bagus'
    elif rating >= 5:
        result['Rating Kategori'] = 'Normal'
    else:
        result['Rating Kategori'] = 'Buruk'

    # Tambahkan juga input dropdown apa adanya
    result['Pelayanan'] = data['Pelayanan']
    result['Kualitas Layanan'] = data['Kualitas Layanan']
    result['Kepatuhan Regulasi'] = data['Kepatuhan Regulasi']

    return result
