1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
   Kalau ada beberapa selector yang mengarah ke elemen yang sama, browser milih berdasarkan urutan prioritas: inline style > ID > class/attribute/pseudo-class > element/tag. Kalau masih sama, dipilih yang paling terakhir ditulis.

2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
   Responsive design sangat penting agar tampilan web tetap enak dilihat di berbagai ukuran layar (hp, tablet, laptop). Contoh yang sudah menerapkan: Tokopedia, UI-nya tetap rapi di layar kecil. Yang belum: web PWS Fasilkom, sampe sekarang masih harus geser-geser layar.
   

3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
   -Margin: jarak di luar elemen, bikin space antar elemen.
   -Border: garis pembatas di sekitar elemen.
   -Padding: jarak antara isi elemen dengan bordernya.

   Semua bisa diatur pakai CSS, misalnya margin: 10px; padding: 5px; border: 1px solid black;.

4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
   - Flexbox: buat atur elemen dalam satu baris/kolom biar fleksibel, gampang align tengah.
   - Grid Layout: lebih cocok buat layout yang kompleks, karena bisa bikin struktur baris dan kolom yang lebih teratur.


5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!
   1. Pertama-tama, saya mulai dengan menambahkan file statis seperti CSS dan menghubungkannya ke template agar tampilan halaman lebih rapi. Setelah itu, saya membuat komponen navbar upaya bisa menyesuaikan baik di layar desktop maupun mobile.
   2. Selanjutnya, saya menambahkan kartu berita dengan styling Tailwind agar produk lebih mudah dibaca dan terlihat menarik. Lalu, saya membuat styling untuk halaman detail yang muncul ketika tombol “read more” ditekan, sehingga pengguna bisa melihat isi lengkap dari berita atau produk.
   3. Setelah tampilan selesai, saya melanjutkan dengan menambahkan fitur edit dan delete. Caranya adalah dengan membuat view, URL, serta template baru yang mendukung fungsi tersebut. Tombol aksi hanya akan muncul pada data yang dibuat oleh pengguna yang sedang login, sehingga ada pembatasan akses.