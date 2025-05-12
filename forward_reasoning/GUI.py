import tkinter as tk
from tkinter import ttk, messagebox

from forward_reasoning.Rules import rules
from forward_reasoning.inferensi import infer  
from forward_reasoning.CF import *
from forward_reasoning.kategory import *


class ISPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Evaluasi ISP (Forward Reasoning + Kategori)")
        self.inputs = {}

        self.create_form()
        self.result_label = ttk.Label(self.root, text="", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

    def create_form(self):
        form_fields = [
            ("RTO (x/bulan)", "RTO", "entry"),
            ("Bandwidth (Mbps)", "Bandwidth", "entry"),
            ("Harga (Rp)", "Harga", "entry"),
            ("Pelayanan", "Pelayanan", ["Baik", "Buruk"]),
            ("Rating (0-10)", "Rating", "entry"),
            ("Kualitas Layanan", "Kualitas Layanan", ["Bagus", "Buruk"]),
            ("Kepatuhan Regulasi", "Kepatuhan Regulasi", ["Memenuhi aturan", "Tidak memenuhi aturan"])
        ]

        for label, key, widget in form_fields:
            frame = ttk.Frame(self.root)
            frame.pack(padx=10, pady=3, fill="x")

            ttk.Label(frame, text=label, width=25).pack(side="left")
            var = tk.StringVar()
            self.inputs[key] = var

            if widget == "entry":
                entry = ttk.Entry(frame, textvariable=var)
                entry.pack(side="left", fill="x", expand=True)

                if key == "Harga":
                    entry.bind("<KeyRelease>", lambda e, v=var: self.format_rupiah(e, v))
            else:
                ttk.Combobox(frame, textvariable=var, values=widget, state="readonly").pack(side="left", fill="x",
                                                                                            expand=True)

        # Pilih metode inferensi
        frame = ttk.Frame(self.root)
        frame.pack(padx=10, pady=3, fill="x")
        ttk.Label(frame, text="Metode Inferensi", width=25).pack(side="left")
        self.method_var = tk.StringVar(value="Forward Reasoning")
        ttk.Combobox(frame, textvariable=self.method_var,
                     values=["Forward Reasoning", "Certainty Factor"],
                     state="readonly").pack(side="left", fill="x", expand=True)

        ttk.Button(self.root, text="Evaluasi", command=self.submit).pack(pady=10)

    def format_rupiah(self, event, var):
        value = var.get().replace(".", "").replace(",", "")
        if value.isdigit():
            formatted = "{:,}".format(int(value)).replace(",", ".")
            var.set(formatted)

    def submit(self):
        data = {}
        for key, var in self.inputs.items():
            val = var.get().strip()
            if not val:
                messagebox.showerror("Error", f"{key} harus diisi")
                return

            if key == "Harga":
                val = val.replace(".", "")  # hapus titik sebelum dikonversi ke int

            data[key] = val

        try:
            method = self.method_var.get()

            if method == "Certainty Factor":
                engine = CertaintyFactorEngine(rules)
                data_terkategori = kategorikan_input(data)  # <-- Tambahkan ini
                hasil_cf = engine.infer(data_terkategori)  # <-- Kirim ke CF engine
                print(f"Data yang diberikan untuk inferensi: {data}")
                if hasil_cf:
                    hasil_text = "\n".join(f"{k}: CF = {round(v, 4)}" for k, v in hasil_cf.items())
                    self.result_label.config(text="Hasil: " + max(hasil_cf, key=hasil_cf.get))
                    messagebox.showinfo("Hasil Evaluasi", f"Hasil:\n{hasil_text}")
                else:
                    self.result_label.config(text="Tidak ada kesimpulan")
                    messagebox.showinfo("Hasil Evaluasi", "Tidak ada kesimpulan berdasarkan data.")
            else:
                result, inferred, explanation = infer(data)
                penjelasan = "\n".join(explanation)
                self.result_label.config(text=f"Hasil: {result}")
                messagebox.showinfo("Hasil Evaluasi", f"Hasil: {result}\n\nPenjelasan:\n{penjelasan}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal proses data: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ISPApp(root)
    root.mainloop()
