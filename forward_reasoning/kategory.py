
def kategorikan_input(data):
    # Stabilitas Jaringan: RTO
    rto = int(data['RTO'])
    data['Stabilitas Jaringan'] = 'Baik' if rto <= 2 else 'Buruk'

    # Kapasitas Bandwidth (Mbps)
    bw = float(data['Bandwidth'])
    if bw > 50:
        data['Kapasitas Bandwidth'] = 'Besar'
    elif bw >= 20:
        data['Kapasitas Bandwidth'] = 'Sedang'
    else:
        data['Kapasitas Bandwidth'] = 'Rendah'

    # Harga (Rp)
    harga = int(data['Harga'])
    if harga < 100000:
        data['Harga Kategori'] = 'Murah'
    elif harga <= 300000:
        data['Harga Kategori'] = 'Standar'
    else:
        data['Harga Kategori'] = 'Mahal'

    # Rating (0–10)
    rating = float(data['Rating'])
    if rating >= 8:
        data['Rating Kategori'] = 'Bagus'
    elif rating >= 5:
        data['Rating Kategori'] = 'Normal'
    else:
        data['Rating Kategori'] = 'Buruk'

    return data
