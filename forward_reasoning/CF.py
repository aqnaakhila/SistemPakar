from forward_reasoning.kategory import kategorikan_input

class RuleCF:
    def __init__(self, kondisi, kesimpulan, cf):
        self.kondisi = kondisi  # Dict: {atribut: nilai}
        self.kesimpulan = kesimpulan
        self.cf = cf  # Nilai Certainty Factor (0–1)



class CertaintyFactorEngine:
    def __init__(self, rules):
        self.rules = rules

    def infer(self, data_input):
        data = kategorikan_input(data_input)

        # Tambahkan inferensi awal agar data punya atribut seperti di rule
        if data['Stabilitas Jaringan'] == 'Baik' and data['Kapasitas Bandwidth'] in ['Besar', 'Sedang']:
            data['Layanan Teknis'] = 'Tidak perlu upgrade kualitas'
        else:
            data['Layanan Teknis'] = 'perlu Upgrade kualitas'

        if data['Pelayanan'] == 'Baik':
            data['Strategi Bisnis'] = 'Tidak perlu perbaikan'
        else:
            data['Strategi Bisnis'] = 'Perlu perbaikan'

        if data['Rating Kategori'] in ['Bagus', 'Normal'] and data['Kualitas Layanan'] == 'Bagus':
            data['Kepuasan Pelanggan'] = 'Pelanggan puas'
        else:
            data['Kepuasan Pelanggan'] = 'Pelanggan tidak puas'

        hasil_cf = {}

        for rule in self.rules:
            print("Mencocokkan dengan rule:", rule.kondisi)
            print("Data saat ini:", data)
            cocok = all(data.get(attr) == value for attr, value in rule.kondisi.items())
            if cocok:
                if rule.kesimpulan in hasil_cf:
                    existing_cf = hasil_cf[rule.kesimpulan]
                    hasil_cf[rule.kesimpulan] = existing_cf + rule.cf * (1 - existing_cf)
                else:
                    hasil_cf[rule.kesimpulan] = rule.cf

        return hasil_cf



# === Daftar aturan CF ===
rules = [
    RuleCF({
        'Layanan Teknis': 'perlu Upgrade kualitas',
        'Strategi Bisnis': 'Tidak perlu perbaikan',
        'Kepatuhan Regulasi': 'Memenuhi aturan',
        'Kepuasan Pelanggan': 'Pelanggan puas'
    }, 'ISP Perlu Peningkatan', 0.8),

    RuleCF({
        'Layanan Teknis': 'perlu Upgrade kualitas',
        'Strategi Bisnis': 'Tidak perlu perbaikan',
        'Kepatuhan Regulasi': 'Memenuhi aturan',
        'Kepuasan Pelanggan': 'Pelanggan tidak puas'
    }, 'ISP Bermasalah', 0.9),

    RuleCF({
        'Layanan Teknis': 'perlu Upgrade kualitas',
        'Strategi Bisnis': 'Perlu perbaikan',
        'Kepuasan Pelanggan': 'Pelanggan puas'
    }, 'ISP Perlu Peningkatan', 0.7),

    RuleCF({
        'Layanan Teknis': 'perlu Upgrade kualitas',
        'Strategi Bisnis': 'Perlu perbaikan',
        'Kepuasan Pelanggan': 'Pelanggan tidak puas'
    }, 'ISP Bermasalah', 0.95),

    RuleCF({
        'Layanan Teknis': 'perlu Upgrade kualitas',
        'Strategi Bisnis': 'Perlu perbaikan',
        'Kepatuhan Regulasi': 'Tidak memenuhi aturan'
    }, 'ISP Bermasalah', 0.85),

    RuleCF({
        'Layanan Teknis': 'Tidak perlu upgrade kualitas',
        'Strategi Bisnis': 'Tidak perlu perbaikan',
        'Kepuasan Pelanggan': 'Pelanggan puas'
    }, 'ISP Berkualitas Baik', 0.95),

    RuleCF({
        'Layanan Teknis': 'Tidak perlu upgrade kualitas',
        'Strategi Bisnis': 'Tidak perlu perbaikan',
        'Kepuasan Pelanggan': 'Pelanggan tidak puas'
    }, 'ISP Perlu Peningkatan', 0.75),

    RuleCF({
        'Layanan Teknis': 'Tidak perlu upgrade kualitas',
        'Strategi Bisnis': 'Perlu perbaikan',
        'Kepatuhan Regulasi': 'Memenuhi aturan',
        'Kepuasan Pelanggan': 'Pelanggan puas'
    }, 'ISP Berkualitas Baik', 0.85),

    RuleCF({
        'Layanan Teknis': 'Tidak perlu upgrade kualitas',
        'Strategi Bisnis': 'Perlu perbaikan',
        'Kepatuhan Regulasi': 'Memenuhi aturan',
        'Kepuasan Pelanggan': 'Pelanggan puas'
    }, 'ISP Perlu Perbaikan', 0.65),

    RuleCF({
        'Layanan Teknis': 'Tidak perlu upgrade kualitas',
        'Strategi Bisnis': 'Perlu perbaikan',
        'Kepatuhan Regulasi': 'Tidak memenuhi aturan',
        'Kepuasan Pelanggan': 'Pelanggan puas'
    }, 'ISP Perlu Perbaikan', 0.6),

    RuleCF({
        'Layanan Teknis': 'Tidak perlu upgrade kualitas',
        'Strategi Bisnis': 'Perlu perbaikan',
        'Kepatuhan Regulasi': 'Tidak memenuhi aturan',
        'Kepuasan Pelanggan': 'Pelanggan tidak puas'
    }, 'ISP Bermasalah', 0.95),
]

# Untuk ekspor
__all__ = ["CertaintyFactorEngine", "rules"]
