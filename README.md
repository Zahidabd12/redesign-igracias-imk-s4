# 🎨 Redesign Dashboard Academic iGracias Telkom University

Repository ini berisi *source code High-Fidelity Mockup* (HTML/CSS/JS) untuk proyek redesain antarmuka portal akademik **iGRACIAS Telkom University**. Proyek ini dikembangkan secara kolaboratif sebagai bagian dari pemenuhan tugas mata kuliah **Interaksi Manusia Komputer (IMK / HCI)**.

---

## 👥 Tim Pengembang

Proyek ini disusun oleh:
| Nama | NIM |
| :--- | :--- |
| **Avrio De Galyn Athar** | 103102400032 |
| **Zahid Abdullah Nur M.** | 103102400034 |
| **Rafif Fikri** | 103102400068 |
| **Al Falaq Axcellio Gais Blantran de Rozari** | 103102400074 |

---

## 🌐 Live Demo (Usability Testing)

Anda dapat mengakses dan menguji coba *mockup* interaktif ini secara langsung melalui tautan GitHub Pages berikut:

👉 **[Buka Live Demo Aplikasi](https://Zahidabd12.github.io/redesign-igracias-imk-s4/)**

*(Seluruh fungsi JavaScript antarmuka seperti modal, navigasi sidebar, form feedback, dan filter telah disimulasikan agar dapat digunakan secara fungsional untuk keperluan **Usability Testing**).*

---

## 🚀 Daftar Halaman & Fitur Utama

Aplikasi ini dibangun murni menggunakan **Vanilla HTML, Custom Properties CSS (Tokens), dan JavaScript murni** (tanpa framework/library pihak ketiga) guna menjaga performa yang ringan dan kemudahan modifikasi.

| Halaman | Keterangan Fungsi |
| :--- | :--- |
| 🔑 `index.html` / `login.html` | **Otentikasi:** Halaman pertama (*Entry Point*) berupa *login* SSO dengan simulasi validasi input dan *shake animation*. |
| 🏠 `landing_page.html` | **Dashboard Utama:** Halaman pertama setelah berhasil *login*. Menampilkan *Hero Banner*, statistik KPI (IPK/SKS), Jadwal Hari Ini, dan tabel *deadline*. |
| 👤 `akun.html` | **Profil & Pengaturan:** Menampilkan progres kelengkapan profil mahasiswa dan fitur simulasi *edit* data diri. |
| 📋 `presensi.html` | **Kehadiran:** Fitur simulasi *scanner* QR Code dan *donut chart* ringkasan kehadiran. |
| 💻 `elearning.html` | **E-Learning (LMS):** Ruang kelas digital, filter pencarian mata kuliah, dan simulasi *upload* tugas. |
| 💬 `bimbingan.html` | **Log Bimbingan:** Modul penjadwalan (*Daring/Luring*) dan log riwayat bimbingan akademik dengan Dosen Wali. |
| 💸 `pembayaran.html` | **Administrasi Keuangan:** *Live countdown* tagihan UKT aktif dan riwayat histori pembayaran. |
| 🏢 `asrama.html` | **Fasilitas:** Modul reservasi berbagai fasilitas kampus *(Gym, Ruang Diskusi, Laundry)*. |
| 🎓 `nilai.html` | **Transkrip Akademik:** *Bar chart* perolehan SKS dan KHS (Kartu Hasil Studi) mahasiswa per semester. |

---

## ✨ Highlight Prinsip UI/UX yang Diterapkan

1. **Struktur Tata Letak (*Zoning & Dashboard Layout*)**  
   Pemisahan jelas antara *Sidebar Vertikal* statis (sebagai jangkar navigasi) dan *Kanvas Konten* dinamis yang dibagi menjadi zona-zona hierarki: Top (Prioritas Tinggi), Middle (Tugas Harian), dan Bottom (Tabel *Deadline*).
2. **Keseimbangan Visual Asimetris (*Asymmetric Balance*)**  
   Menggunakan *Sidebar* berwarna padat/gelap untuk mengimbangi bidang konten putih/terang yang luas di sebelah kanan layar, mendistribusikan beban kognitif mata secara merata.
3. **Aksesibilitas & Feedback (*Accessibility*)**  
   Mendukung pergantian **Light Mode / Dark Mode** yang disimpan persisten di browser. Seluruh elemen input/tombol dilengkapi *focus rings* untuk kemudahan navigasi *keyboard*, serta *Toast Notification* setiap kali pengguna menyelesaikan tugas (*action*).
4. **Hierarki Tipografi (*Visual Hierarchy*)**  
   Penggunaan dua kelompok *font* yang kontras (*DM Serif Display* yang tebal untuk angka/sorotan utama, dan *Plus Jakarta Sans* untuk teks deskripsi) agar fokus pengguna terarah secara intuitif dari informasi terbesar ke detail pendukung.
