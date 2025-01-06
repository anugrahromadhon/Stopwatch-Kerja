import tkinter as tk
from tkinter import messagebox
import time
import threading

class PenghitungWaktuKerja:
    def __init__(self, root):
        self.root = root
        self.root.title("Penghitung Waktu Kerja untuk Freelancer")
        self.root.configure(bg="#282C34")

        self.mulai_waktu = None
        self.selesai_waktu = None
        self.jalankan_jam = False

        # Header
        self.label_header = tk.Label(root, text="Penghitung Waktu Kerja", font=("Helvetica", 18, "bold"), fg="#61AFEF", bg="#282C34")
        self.label_header.pack(pady=10)

        # Status
        self.label_status = tk.Label(root, text="Klik 'Mulai' untuk memulai pencatatan waktu.", font=("Helvetica", 12), fg="#ABB2BF", bg="#282C34")
        self.label_status.pack(pady=10)

        # Clock display
        self.label_clock = tk.Label(root, text="00:00:00", font=("Courier New", 24, "bold"), fg="#98C379", bg="#282C34")
        self.label_clock.pack(pady=10)

        # Buttons
        self.tombol_mulai = tk.Button(root, text="Mulai", font=("Helvetica", 12), bg="#98C379", fg="#282C34", command=self.mulai)
        self.tombol_mulai.pack(pady=5)

        self.tombol_selesai = tk.Button(root, text="Selesai", font=("Helvetica", 12), bg="#E06C75", fg="#282C34", command=self.selesai, state=tk.DISABLED)
        self.tombol_selesai.pack(pady=5)

        # Result
        self.label_hasil = tk.Label(root, text="", font=("Helvetica", 12), fg="#ABB2BF", bg="#282C34")
        self.label_hasil.pack(pady=10)

    def update_clock(self):
        while self.jalankan_jam:
            if self.mulai_waktu:
                elapsed = time.time() - self.mulai_waktu
                jam = int(elapsed // 3600)
                menit = int((elapsed % 3600) // 60)
                detik = int(elapsed % 60)
                self.label_clock.config(text=f"{jam:02}:{menit:02}:{detik:02}")
            time.sleep(1)

    def mulai(self):
        self.mulai_waktu = time.time()
        self.jalankan_jam = True
        threading.Thread(target=self.update_clock, daemon=True).start()

        self.label_status.config(text="Pencatatan waktu dimulai. Klik 'Selesai' saat pekerjaan selesai.")
        self.tombol_mulai.config(state=tk.DISABLED)
        self.tombol_selesai.config(state=tk.NORMAL)

    def selesai(self):
        if self.mulai_waktu is None:
            messagebox.showerror("Error", "Anda belum memulai pencatatan waktu.")
            return

        self.jalankan_jam = False
        self.selesai_waktu = time.time()
        durasi = self.selesai_waktu - self.mulai_waktu
        jam = int(durasi // 3600)
        menit = int((durasi % 3600) // 60)
        detik = int(durasi % 60)

        self.label_hasil.config(text=f"Durasi kerja: {jam} jam, {menit} menit, {detik} detik.")
        self.label_status.config(text="Klik 'Mulai' untuk memulai pencatatan waktu lagi.")
        self.label_clock.config(text="00:00:00")
        self.tombol_mulai.config(state=tk.NORMAL)
        self.tombol_selesai.config(state=tk.DISABLED)
        self.mulai_waktu = None
        self.selesai_waktu = None

if __name__ == "__main__":
    root = tk.Tk()
    app = PenghitungWaktuKerja(root)
    root.mainloop()
