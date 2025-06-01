# SportsHub - Sistem Manajemen Olahraga

SportsHub adalah aplikasi web yang dibangun menggunakan Flask untuk membantu mengelola aktivitas olahraga, tim, dan acara. Aplikasi ini mengikuti pola MVC (Model-View-Controller) dan menggunakan SQLite sebagai database.

## Fitur

- Mengelola berbagai olahraga dan detailnya
- Melacak tim dan informasi mereka
- Menjadwalkan dan mengelola acara olahraga
- Antarmuka yang ramah pengguna dengan desain Bootstrap

## Struktur Proyek

```
SportsHub/
├── models/
│   ├── sport.py
│   ├── team.py
│   └── event.py
├── views/
│   └── templates/
│       ├── base.html
│       ├── index.html
│       ├── sports/
│       ├── teams/
│       └── events/
├── controllers/
│   ├── sport_controller.py
│   ├── team_controller.py
│   └── event_controller.py
├── static/
├── app.py
└── requirements.txt
```

## Cara Instalasi

1. Clone repository:

```bash
git clone <repository-url>
cd SportsHub
```

2. Buat virtual environment dan aktifkan:

```bash
python -m venv venv
source venv/bin/activate  # Untuk Windows: venv\Scripts\activate
```

3. Install package yang diperlukan:

```bash
pip install -r requirements.txt
```

4. Inisialisasi database:

```bash
flask db init
flask db migrate
flask db upgrade
```

5. Jalankan aplikasi:

```bash
python app.py
```

Aplikasi akan tersedia di `http://localhost:5000`

## Cara Penggunaan

1. **Manajemen Olahraga**

   - Melihat semua olahraga
   - Menambah olahraga baru
   - Mengedit olahraga yang ada
   - Menghapus olahraga

2. **Manajemen Tim**

   - Melihat semua tim
   - Menambah tim baru
   - Mengedit informasi tim
   - Menghapus tim

3. **Manajemen Acara**
   - Melihat semua acara
   - Menjadwalkan acara baru
   - Mengedit detail acara
   - Menghapus acara

## Urutan Penggunaan

1. Pertama, buat beberapa olahraga melalui halaman Sports
2. Setelah ada olahraga, Anda bisa membuat tim yang terkait dengan olahraga tersebut
3. Setelah ada tim, Anda bisa membuat acara yang melibatkan tim tersebut
