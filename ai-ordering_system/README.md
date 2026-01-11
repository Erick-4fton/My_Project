# 🤖 Sistem Pemesanan Hotwheels & Gundam Berbasis AI

## 📌 Deskripsi Project
Project ini merupakan **aplikasi web statis** yang mengintegrasikan **Artificial Intelligence (AI)** untuk membantu pengguna mendapatkan **rekomendasi produk Hotwheels dan Gundam** berdasarkan pertanyaan dalam bahasa natural.

Project ini dibuat untuk memenuhi **Ujian Akhir Semester (UAS)** dengan objektif utama:
> **“Integrate Application with AI”**

AI akan memproses input pengguna dan memberikan rekomendasi produk secara cerdas tanpa menggunakan database.

---

## 🎯 Tujuan Aplikasi
- Memberikan rekomendasi produk secara otomatis menggunakan AI
- Membantu user memilih produk sesuai kebutuhan dan budget
- Menerapkan integrasi AI ke dalam aplikasi web
- Mengimplementasikan konsep AI modern berbasis API

---

## 🧠 Teknologi yang Digunakan
### Backend
- **Python 3**
- **FastAPI** – REST API server
- **LangChain** – Orkestrasi prompt & AI logic
- **OpenRouter API** – AI gateway
- **Model AI:** `mistralai/mistral-7b-instruct:free`

### Frontend
- **HTML5**
- **CSS3** (UI modern & responsive)
- **JavaScript (Fetch API)**

### AI Model
- **Mistral 7B Instruct (Free Tier)**
- Berjalan di cloud melalui OpenRouter
- Tidak membutuhkan GPU lokal

---

## 📦 Fitur Utama
- 💬 Chat AI untuk rekomendasi produk
- 🧸 Katalog statis 20 produk
  - 10 Gundam
  - 10 Hotwheels
- 🔍 Rekomendasi berdasarkan:
  - Kategori
  - Harga
  - Kebutuhan user
- ⚡ Respon cepat dan real-time

---

## 🔄 Alur Kerja Sistem (Workflow)
1. User membuka halaman web
2. User memasukkan pertanyaan (contoh: *"Gundam untuk pemula di bawah 200 ribu"*)
3. Frontend mengirim request ke Backend (FastAPI)
4. Backend meneruskan prompt ke AI (OpenRouter)
5. AI memproses dan memberikan rekomendasi
6. Jawaban dikembalikan dan ditampilkan ke user

---

## 🗂 Struktur Folder Project
```
ai-ordering-system/
│
├── backend/
│   ├── main.py
│   ├── ai_chain.py
│   ├── product_data.py
│   ├── requirements.txt
│   ├── .env.example
│   └── venv/            (tidak diupload)
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── README.md
└── .gitignore
```

---

## 🔐 Konfigurasi Environment
Buat file `.env` berdasarkan `.env.example`:
```
OPENROUTER_API_KEY=sk-xxxxxxxx
OPENROUTER_MODEL=mistralai/mistral-6b-instruct:free
```

---

## ▶️ Cara Menjalankan Aplikasi
### 1️⃣ Aktifkan Virtual Environment
```bash
cd backend
source venv/bin/activate
```

### 2️⃣ Install Dependency
```bash
pip install -r requirements.txt
```

### 3️⃣ Jalankan Server Backend
```bash
uvicorn main:app --reload
```

### 4️⃣ Buka Frontend
Buka file berikut di browser:
```
frontend/index.html
```

---

## 🧪 Contoh Pertanyaan AI
- "Gundam yang cocok untuk pemula"
- "Hotwheels di bawah 50 ribu"
- "Rekomendasi Gundam MG terbaik"
- "Mainan koleksi yang murah"

---

## 📸 Dokumentasi Aplikasi
> Screenshot / Video demo aplikasi dapat dilihat pada repository GitHub

---

## 🧩 Alasan Pemilihan Model AI
Model **Mistral 7B Instruct** dipilih karena:
- Mendukung percakapan natural
- Cocok untuk sistem rekomendasi berbasis teks
- Performa stabil
- Gratis tanpa kartu kredit
- Tersedia melalui OpenRouter API

---

## 🚫 Batasan Aplikasi
- Tidak menggunakan database
- Data produk bersifat statis
- Fokus pada rekomendasi berbasis teks

---

## 🏁 Kesimpulan
Project ini berhasil mengimplementasikan integrasi AI ke dalam aplikasi web secara efektif. AI digunakan untuk meningkatkan pengalaman pengguna melalui rekomendasi produk yang relevan dan interaktif, sesuai dengan objektif mata kuliah.

---

## 👨‍🎓 Informasi Mahasiswa
- **Nama:** ……………………
- **NIM:** ……………………
- **Mata Kuliah:** ……………………
- **Dosen Pengampu:** ……………………

---

✨ *Project ini dikembangkan untuk keperluan akademik (UAS)*

