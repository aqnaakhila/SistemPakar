class CertaintyFactorEngine:
    def __init__(self, rules):
        self.rules = rules

    def infer(self, facts):
        known_facts = facts.copy()  # fakta awal dari user
        inferred_cf = {}            # hasil kesimpulan + nilai CF
        fired_rules = set()         # agar tidak looping terus

        while True:
            triggered = False
            for i, rule in enumerate(self.rules):
                if i in fired_rules:
                    continue

                premises = rule["if"]
                conclusion = rule["then"]
                cf_rule = rule["cf"]

                # Cek apakah semua premis tersedia di known_facts
                cf_values = []
                all_matched = True
                for key, expected_val in premises:
                    actual_val = known_facts.get(key)
                    if actual_val and actual_val.lower() == expected_val.lower():
                        cf_values.append(1.0)
                    else:
                        all_matched = False
                        break

                if all_matched:
                    triggered = True
                    fired_rules.add(i)
                    cf_combined = min(cf_values) * cf_rule

                    # Gabungkan jika sudah ada sebelumnya
                    if conclusion in inferred_cf:
                        inferred_cf[conclusion] = self.combine_cf(inferred_cf[conclusion], cf_combined)
                    else:
                        inferred_cf[conclusion] = cf_combined

                    # Simpan kesimpulan sebagai fakta baru
                    if "=" in conclusion:
                        key, val = [s.strip() for s in conclusion.split("=")]
                        known_facts[key] = val

            if not triggered:
                break

        return inferred_cf

    def combine_cf(self, cf1, cf2):
        # Gabungkan dua CF sesuai teori
        if cf1 >= 0 and cf2 >= 0:
            return cf1 + cf2 * (1 - cf1)
        elif cf1 < 0 and cf2 < 0:
            return cf1 + cf2 * (1 + cf1)
        else:
            return (cf1 + cf2) / (1 - min(abs(cf1), abs(cf2)))
