# Penghitung Waktu Kerja

## Deskripsi
"Penghitung Waktu Kerja" adalah sebuah aplikasi berbasis GUI yang membantu freelancer untuk mencatat durasi waktu kerja mereka dengan mudah. Program ini memiliki fitur seperti pencatatan waktu mulai dan selesai, tampilan jam berjalan secara real-time, dan laporan durasi kerja.

Aplikasi ini dirancang dengan antarmuka yang menarik menggunakan kombinasi warna yang modern, dan menampilkan animasi jam yang terus berjalan selama pencatatan waktu aktif.

## Fitur Utama
1. **Mulai Pencatatan Waktu**:
   - Klik tombol "Mulai" untuk memulai pencatatan waktu kerja.
   
2. **Selesai Pencatatan Waktu**:
   - Klik tombol "Selesai" untuk menghentikan pencatatan waktu dan melihat durasi total kerja.

3. **Tampilan Waktu Real-Time**:
   - Jam berjalan real-time yang diperbarui setiap detik selama pencatatan waktu.

4. **Antarmuka Modern**:
   - Kombinasi warna dan layout menarik untuk pengalaman pengguna yang lebih baik.

## Persyaratan Sistem
- Python 3.7 atau lebih baru
- Modul Python:
  - `tkinter` (bawaan Python)
  - `threading`
  - `time`

## Cara Menjalankan Program
1. Pastikan Python telah terinstal di komputer Anda.
2. Simpan file kode ke dalam sebuah file bernama `main.py`.
3. Jalankan program dengan perintah berikut di terminal atau command prompt:
   ```
   python main.py
   ```
4. Antarmuka aplikasi akan terbuka, dan Anda dapat mulai menggunakan aplikasi.

## Panduan Penggunaan
1. Klik tombol **"Mulai"** untuk memulai pencatatan waktu kerja.
2. Saat selesai bekerja, klik tombol **"Selesai"** untuk menghentikan pencatatan waktu dan melihat durasi kerja.
3. Untuk memulai pencatatan waktu baru, klik kembali tombol **"Mulai"**.

## Tampilan Aplikasi
### Header dan Status:
- Teks "Penghitung Waktu Kerja" di bagian atas.
- Informasi status yang berubah sesuai aktivitas pengguna.

### Tombol:
- Tombol "Mulai" dengan warna hijau.
- Tombol "Selesai" dengan warna merah (aktif setelah waktu dimulai).

### Hasil:
- Durasi kerja ditampilkan setelah tombol "Selesai" ditekan.

## Struktur Kode
- **`PenghitungWaktuKerja`**:
  - Kelas utama yang menangani GUI dan logika aplikasi.
  - Fungsi:
    - `update_clock()`: Memperbarui tampilan waktu secara real-time.
    - `mulai()`: Memulai pencatatan waktu.
    - `selesai()`: Menghentikan pencatatan waktu dan menghitung durasi kerja.

## Contoh Output
- Sebelum dimulai: "00:00:00"
- Setelah selesai: "Durasi kerja: 2 jam, 30 menit, 15 detik."

## Lisensi
Program ini bersifat open-source dan dapat digunakan bebas untuk kebutuhan pribadi atau pengembangan lebih lanjut.

