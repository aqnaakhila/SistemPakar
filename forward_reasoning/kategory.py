def kategorikan_input(data):
    result = {}

    # Stabilitas Jaringan: RTO
    rto = int(data['RTO'])
    result['Stabilitas Jaringan'] = 'Baik' if rto <= 2 else 'Buruk'
    print(f"rto : {rto}")

    # Kapasitas Bandwidth (Mbps)
    bw = float(data['Bandwidth'])
    if bw > 50:
        result['Kapasitas Bandwidth'] = 'Besar'
    elif bw >= 20:
        result['Kapasitas Bandwidth'] = 'Sedang'
    else:
        result['Kapasitas Bandwidth'] = 'Rendah'
    print(f"bandwith : {bw}")

    # Harga (Rp)
    harga = int(data['Harga'])
    if harga < 100000:
        result['Harga Kategori'] = 'Murah'
    elif harga <= 300000:
        result['Harga Kategori'] = 'Standar'
    else:
        result['Harga Kategori'] = 'Mahal'
    print(f"harga : {harga}")

    # Rating (0–10)
    rating = float(data['Rating'])
    if rating >= 8:
        result['Rating Kategori'] = 'Bagus'
    elif rating >= 5:
        result['Rating Kategori'] = 'Normal'
    else:
        result['Rating Kategori'] = 'Buruk'
    print(f"rating : {rating}")

    # Tambahkan juga input dropdown apa adanya
    result['Pelayanan'] = data['Pelayanan']
    print(f"Pelayanan :{result['Pelayanan']}")
    result['Kualitas Layanan'] = data['Kualitas Layanan']
    print(f"Kualitas Layanan :{result['Kualitas Layanan']}")
    result['Kepatuhan Regulasi'] = data['Kepatuhan Regulasi']
    print(f"Kepatuhan Regulasi :{result['Kepatuhan Regulasi']}")

    return result