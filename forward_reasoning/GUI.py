import tkinter as tk
from tkinter import ttk, messagebox
from forward_reasoning.inferensi import infer  

class ISPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Evaluasi ISP (Forward Reasoning + Kategori)")
        self.inputs = {}

        self.create_form()
        self.result_label = ttk.Label(self.root, text="", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

    def create_form(self):
        numeric_fields = {
            "RTO (x/bulan)": "RTO",
            "Bandwidth (Mbps)": "Bandwidth",
            "Harga (Rp)": "Harga",
            "Rating (0-10)": "Rating"
        }

        for label, key in numeric_fields.items():
            frame = ttk.Frame(self.root)
            frame.pack(padx=10, pady=3, fill="x")
            ttk.Label(frame, text=label, width=25).pack(side="left")
            var = tk.StringVar()
            self.inputs[key] = var

            entry = ttk.Entry(frame, textvariable=var)
            entry.pack(side="left", fill="x", expand=True)

            # Format Harga saat diketik
            if key == "Harga":
                entry.bind("<KeyRelease>  ",lambda e, v=var: self.format_rupiah(e, v),)

        dropdown_fields = {
            "Pelayanan": ["Baik", "Buruk"],
            "Kualitas Layanan": ["Bagus", "Buruk"],
            "Kepatuhan Regulasi": ["Memenuhi aturan", "Tidak memenuhi aturan"]
        }

        for label, options in dropdown_fields.items():
            frame = ttk.Frame(self.root)
            frame.pack(padx=10, pady=3, fill="x")
            ttk.Label(frame, text=label, width=25).pack(side="left")
            var = tk.StringVar()
            self.inputs[label] = var
            ttk.Combobox(frame, textvariable=var, values=options, state="readonly").pack(side="left", fill="x", expand=True)

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
            result, inferred, explanation = infer(data)
            penjelasan = "\n".join(explanation)
            messagebox.showinfo("Hasil Evaluasi", f"Hasil: {result}\n\nPenjelasan:\n{penjelasan}")
            self.result_label.config(text=f"Hasil: {result}")
        except Exception as e:
            messagebox.showerror("Error", f"Gagal proses data: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ISPApp(root)
    root.mainloop()
