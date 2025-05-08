import tkinter as tk
from tkinter import ttk, messagebox

# --- Aturan disederhanakan dalam bentuk python-friendly ---
rules = [
    {
        "if": {
            "Layanan Teknis": "Upgrade kualitas",
            "Strategi Bisnis": "Tidak perlu perbaikan",
            "Kepatuhan Regulasi": "Memenuhi aturan",
            "Kepuasan Pelanggan": "Pelanggan puas"
        },
        "then": "ISP Berkualitas Baik"
    },
    {
        "if": {
            "Layanan Teknis": "Upgrade kualitas",
            "Strategi Bisnis": "Tidak perlu perbaikan",
            "Kepatuhan Regulasi": "Memenuhi aturan",
            "Kepuasan Pelanggan": "Pelanggan tidak puas"
        },
        "then": "ISP Bermasalah"
    },
    {
        "if": {
            "Layanan Teknis": "Upgrade kualitas",
            "Strategi Bisnis": "Perlu perbaikan",
            "Kepuasan Pelanggan": "Pelanggan puas"
        },
        "then": "ISP Perlu Peningkatan"
    },
    {
        "if": {
            "Layanan Teknis": "Tidak perlu upgrade kualitas",
            "Strategi Bisnis": "Tidak perlu perbaikan",
            "Kepuasan Pelanggan": "Pelanggan puas"
        },
        "then": "ISP Berkualitas Baik"
    },
    {
        "if": {
            "Layanan Teknis": "Tidak perlu upgrade kualitas",
            "Strategi Bisnis": "Perlu perbaikan",
            "Kepatuhan Regulasi": "Tidak memenuhi aturan",
            "Kepuasan Pelanggan": "Pelanggan tidak puas"
        },
        "then": "ISP Bermasalah"
    },
    # Tambahkan aturan lainnya sesuai file rules.txt bila perlu
]

# --- BACKWARD REASONING LOGIC ---
def backward_reason(goal, facts):
    for rule in rules:
        if rule["then"] == goal:
            required = rule["if"]
            needed = []
            for k, v in required.items():
                if k not in facts:
                    needed.append((k, v))
                elif facts[k] != v:
                    break
            else:
                if not needed:
                    return True, []
                else:
                    return None, needed
    return False, []

# --- GUI ---
class BackwardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Backward Reasoning - Evaluasi ISP")
        self.facts = {}
        self.create_ui()

    def create_ui(self):
        self.goal_var = tk.StringVar()
        ttk.Label(self.root, text="Pilih Tujuan:").pack(pady=5)
        self.goal_box = ttk.Combobox(self.root, textvariable=self.goal_var, state="readonly",
        values=["ISP Berkualitas Baik", "ISP Bermasalah", "ISP Perlu Peningkatan"])
        self.goal_box.pack(pady=5)

        self.query_frame = ttk.LabelFrame(self.root, text="Pertanyaan")
        self.query_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.result_label = ttk.Label(self.root, text="", font=("Arial", 12, "bold"))
        self.result_label.pack(pady=10)

        self.submit_btn = ttk.Button(self.root, text="Mulai Reasoning", command=self.start_reasoning)
        self.submit_btn.pack(pady=5)

    def ask_questions(self, questions):
        for widget in self.query_frame.winfo_children():
            widget.destroy()

        self.question_vars = {}
        for attr, val in questions:
            label = ttk.Label(self.query_frame, text=f"{attr}? (diinginkan: {val})")
            label.pack(anchor="w", padx=5, pady=2)
            var = tk.StringVar()
            entry = ttk.Combobox(self.query_frame, textvariable=var, values=[val, "lainnya"], state="readonly")
            entry.pack(fill="x", padx=5)
            self.question_vars[attr] = var

        confirm_btn = ttk.Button(self.query_frame, text="Konfirmasi Jawaban", command=self.confirm_answers)
        confirm_btn.pack(pady=10)

    def confirm_answers(self):
        for k, var in self.question_vars.items():
            ans = var.get()
            if ans == "":
                messagebox.showerror("Error", "Isi semua pertanyaan")
                return
            self.facts[k] = ans
        self.start_reasoning()

    def start_reasoning(self):
        goal = self.goal_var.get()
        if not goal:
            messagebox.showerror("Error", "Pilih dulu tujuan")
            return

        result, questions = backward_reason(goal, self.facts)

        if result is True:
            self.result_label.config(text=f"Hasil: {goal} ✅")
        elif result is False:
            self.result_label.config(text=f"Tujuan '{goal}' tidak bisa disimpulkan ❌")
        else:
            self.result_label.config(text="Membutuhkan input tambahan...")
            self.ask_questions(questions)

# --- RUN APP ---
if __name__ == "__main__":
    root = tk.Tk()
    app = BackwardApp(root)
    root.mainloop()
