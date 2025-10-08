1. Apa perbedaan antara synchronous request dan asynchronous request?
   Synchronous merupakan model tradisional. Saat browser mengirim request ke server (misalnya, dengan mengklik link atau submit form), ia akan mengunci seluruh halaman dan menunggu sampai server memberikan respons penuh berupa halaman HTML baru. Selama menunggu, 

   Asynchronous adalah model yang digunakan oleh AJAX. Saat browser mengirim request, ia melakukannya di latar belakang tanpa mengunci halaman. Pengguna bisa terus berinteraksi dengan website menggulir, mengklik tombol lain sementara browser menunggu respons dari server. Ketika respons (seperti JSON) tiba, hanya bagian tertentu dari halaman yang diperbarui.

2. Bagaimana AJAX bekerja di Django (alur request–response)?
   1. Aksi Pengguna (Frontend): Pengguna melakukan aksi di halaman web, misalnya mengklik tombol "Add Product".
   2. JavaScript Mengambil Alih: Sebuah fungsi JavaScript (misalnya, addProduct()) dipanggil. Fungsi ini mencegah aksi default browser (yang akan me-reload halaman).
   3. Fetch Request: JavaScript menggunakan fetch() untuk mengirim request HTTP (biasanya POST) ke sebuah URL endpoint khusus di Django (misalnya, /add-product-ajax/). Data dari form dikirim bersama request ini.
   4. Django Menerima (Backend): URL tersebut diarahkan ke sebuah view khusus AJAX di views.py (misalnya, add_product_ajax).
   5. Proses di View: View tersebut memproses data yang diterima, berinteraksi dengan database (misalnya, Product.objects.create(...)), lalu menyimpan produk baru.
   6. JsonResponse: Alih-alih me-render template HTML, view ini mengembalikan JsonResponse yang berisi data relevan (misalnya, status sukses atau data produk yang baru dibuat).
   7. JavaScript Menerima Respons: Fungsi fetch() di JavaScript menerima respons JSON ini dari server.
   8. Pembaruan Tampilan (DOM Manipulation): JavaScript kemudian memperbarui tampilan halaman secara dinamis. Contohnya, ia bisa memanggil fungsi fetchProductsFromServer() lagi untuk mengambil daftar produk terbaru dan me-render ulang hanya bagian grid produk tanpa me-reload seluruh halaman.

3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
   1. Pengalaman Pengguna (UX) yang Lebih Baik: Ini adalah keuntungan terbesar. Aplikasi terasa jauh lebih cepat, mulus, dan responsif karena tidak ada lagi kedipan putih akibat full page reload. Interaksi terasa instan, mirip seperti menggunakan aplikasi desktop atau mobile.
   2. Mengurangi Beban Server: Server tidak perlu lagi me-render seluruh template HTML setiap kali ada aksi kecil. Ia hanya perlu mengirimkan data JSON yang ukurannya jauh lebih kecil, sehingga mengurangi beban kerja dan penggunaan bandwidth.
   3. Peningkatan Performa: Karena hanya data yang relevan yang ditransfer dan hanya bagian kecil dari halaman yang diperbarui, waktu muat dan respons aplikasi menjadi lebih cepat secara keseluruhan.

4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
   1. CSRF Token (Wajib): Serangan Cross-Site Request Forgery (CSRF) tetap menjadi ancaman. Pastikan setiap request POST via AJAX tetap menyertakan CSRF token dari Django. Token ini bisa diambil dari cookie atau diselipkan di dalam HTML, lalu ditambahkan ke header request fetch() oleh JavaScript.
   2. Gunakan HTTPS: Selalu gunakan koneksi HTTPS (SSL/TLS) untuk mengenkripsi data (username dan password) yang dikirim antara browser dan server, sehingga tidak bisa diintip di tengah jalan.
   3. Validasi di Sisi Server: Jangan pernah percaya pada input dari pengguna. Semua validasi (misalnya, apakah password cukup kuat, apakah username sudah ada) harus tetap dilakukan secara menyeluruh di sisi server (views.py), meskipun sudah ada validasi di JavaScript.
   4. Jangan Kirim Informasi Sensitif di Respons: Setelah login berhasil, cukup kirim status sukses. Jangan pernah mengirim kembali data sensitif seperti password di dalam respons JSON.

5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
   1. Responsivitas: Pengguna mendapatkan feedback instan atas aksi mereka. Mengklik "Like" akan langsung mengubah angka tanpa menunggu halaman reload.
   2. Alur Kerja yang Tidak Terputus: Pengguna bisa terus melakukan pekerjaannya tanpa terganggu oleh proses loading halaman. Contohnya, saat mengisi form yang panjang, data bisa disimpan otomatis di latar belakang.
   3. Efisiensi: Pengguna tidak perlu memuat ulang elemen yang sama (seperti header, sidebar, footer) berulang kali, sehingga menghemat waktu dan data.