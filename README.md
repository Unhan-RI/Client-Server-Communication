Berikut adalah README.md dalam Bahasa Indonesia untuk proyek yang Anda berikan:

---

# Sistem Komunikasi Client-Server dengan Load Balancer

Repositori ini berisi implementasi sistem komunikasi client-server berbasis Python. Sistem ini menggunakan dua server dan satu client, dengan load balancer yang bertugas mengatur lalu lintas antara client dan server. Sistem ini juga mencatat detail komunikasi, termasuk waktu koneksi, pertukaran pesan, waktu respons, latensi, dan throughput.

## Struktur

- **client.py**: Menangani operasi di sisi client, termasuk menghubungkan ke server melalui load balancer, serta mengirim dan menerima pesan.
- **server1.py**: Server pertama yang memproses permintaan dari client dan meresponsnya.
- **server2.py**: Server kedua yang juga memproses permintaan dari client dan meresponsnya.
- **load_balancer.py**: Bertindak sebagai perantara antara client dan server, mendistribusikan permintaan client secara merata ke kedua server.
- **client_manager.py**: Mengelola operasi di sisi client dan menangani pencatatan log dari komunikasi yang terjadi.
- **log_manager.py**: Mengelola sistem pencatatan log, yang mencatat detail komunikasi seperti waktu koneksi, pesan yang dikirim dan diterima.
- **log.txt**: Menyimpan log dari semua interaksi antara client, server, dan load balancer, termasuk stempel waktu, status koneksi, dan pengakuan pesan (ACK).

---

## Penjelasan File

### 1. `client.py`
File ini berisi logika untuk operasi di sisi client. Client terhubung ke load balancer dan mengirim pesan, yang kemudian diteruskan ke **server1.py** atau **server2.py** oleh load balancer.

Fitur utama:
- Client secara berulang terhubung ke server, mengirim pesan, dan menunggu pengakuan (ACK).
- Menangani percobaan ulang (retries) dan koneksi ulang bila diperlukan.
- Mensimulasikan pengiriman berbagai jenis pesan.

### 2. `server1.py` & `server2.py`
Kedua file ini mewakili dua server dalam sistem. Setiap server mendengarkan pesan yang masuk dari client melalui load balancer dan merespons dengan ACK (Acknowledgment).

Fitur utama:
- Server menerima pesan dari client melalui load balancer.
- Mengirim balasan berupa ACK untuk mengonfirmasi penerimaan pesan.

### 3. `load_balancer.py`
File ini bertindak sebagai load balancer yang mengatur lalu lintas dari client ke server. Load balancer memilih salah satu server (antara **server1.py** dan **server2.py**) untuk memproses permintaan dari client.

Fitur utama:
- Mendistribusikan permintaan secara merata antara kedua server.
- Menjaga agar beban server terdistribusi dengan baik.

### 4. `client_manager.py`
File ini mengelola operasi client, termasuk menangani proses pengiriman dan penerimaan pesan dari server melalui load balancer. Juga bertanggung jawab untuk mencatat setiap aktivitas client dalam sistem log.

Fitur utama:
- Mengatur koneksi client ke server melalui load balancer.
- Menangani pencatatan log komunikasi client.

### 5. `log_manager.py`
File ini bertanggung jawab untuk pencatatan log dari seluruh sistem komunikasi, baik dari sisi client, server, maupun load balancer. Setiap interaksi dicatat dalam **log.txt** dengan informasi waktu dan status.

Fitur utama:
- Mencatat waktu koneksi, pesan yang dikirim dan diterima, serta pengakuan dari server.

### 6. `log.txt`
File ini berisi log dari semua komunikasi yang terjadi dalam sistem. Setiap kali client terhubung ke server melalui load balancer, detailnya dicatat di sini, termasuk waktu koneksi, pesan yang dikirim, dan balasan yang diterima dari server.

Contoh isi log:
```text
Connection: 2024-10-11 19:52:42 - Client connected
Message Sent: 2024-10-11 19:52:42 - HAI IDO
Message Received: 2024-10-11 19:52:42 - ACK from Server 1
```

---

## Cara Menggunakan

1. **Jalankan Server:**
   - Buka terminal dan jalankan server pertama dengan perintah:
     ```bash
     python server1.py
     ```
   - Jalankan server kedua dengan perintah:
     ```bash
     python server2.py
     ```

2. **Jalankan Load Balancer:**
   - Setelah kedua server berjalan, jalankan load balancer dengan perintah:
     ```bash
     python load_balancer.py
     ```

3. **Jalankan Client:**
   - Terakhir, jalankan client dengan perintah:
     ```bash
     python client.py
     ```

4. **Log Aktivitas:**
   - Semua aktivitas komunikasi akan tercatat di file `log.txt`, yang dapat diperiksa untuk melihat detail koneksi dan pesan yang dikirim/diterima.

---



