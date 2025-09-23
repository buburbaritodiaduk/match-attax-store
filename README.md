1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
   AuthenticationForm adalah sebuah form bawaan Django yang dirancang khusus untuk proses autentikasi atau login pengguna di mana ia berfungsi untuk memvalidasi username dan password yang dimasukkan oleh pengguna.

   Kelebihan:
   1. Form ini sudah menangani berbagai aspek keamanan secara otomatis, seperti perlindungan terhadap timing attacks, sehingga tidak perlu membuat logika validasi login dari nol
   2. Mudah digunakan, karena kita cukup impor dari django.contrib.auth.forms dan gunakan di dalam view dan template

   Kekurangan:
   1. Tidak Fleksibel Secara Default
      Form ini secara bawaan dirancang untuk login menggunakan username. Jika kita ingin login menggunakan email, kita perlu melakukan kustomisasi atau membuat form sendiri
   2. Tampilan Standar
      AuthenticationForm hanya menyediakan logika dan struktur dasar. kita tetap harus membuat tampilan HTML dan CSS sendiri

2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?

   Autentikasi: adalah proses memverifikasi identitas
   Otorisasi: adalah proses memberikan hak akses setelah identitas terverifikasi
 
   Autentikasi: Django menanganinya melalui aplikasi django.contrib.auth. Ini mencakup:
      a. Model User: Untuk menyimpan informasi pengguna.
      b. Fungsi authenticate(), login(), logout(): Untuk mengelola sesi login.
      c. Forms: Seperti AuthenticationForm dan UserCreationForm.
   
   Otorisasi: Django mengimplementasikannya melalui sistem permissions (izin) dan decorators:
      a. Decorators: @login_required adalah bentuk otorisasi paling dasar (harus login untuk mengakses halaman). @permission_required('app.can_delete_product') lebih spesifik, memeriksa apakah user punya izin tertentu.
      b. Flags pada Model User: is_staff (bisa akses halaman admin) dan is_superuser (punya semua izin).
      c. Groups & Permissions: bisa membuat grup pengguna (misal: "Editor", "Moderator") di admin panel dan memberikan izin spesifik kepada setiap grup.

3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
   Cookies adalah data kecil yang disimpan langsung di browser pengguna.
   - Kelebihan
      1. Mudah dibuat dan tidak membebani server karena data disimpan di sisi klien (client-side).
      2. Cookies dapat diatur untuk bertahan lama di browser pengguna, bahkan setelah browser ditutup.
      3. Karena data ada di klien, server tidak perlu menyimpan informasi untuk setiap pengguna aktif.
   
   - Kekurangan
      1. Data di dalam cookies dapat dengan mudah dilihat dan diubah oleh pengguna.
      2. Tidak bisa menyimpan data yang besar.
      3. Semua cookies untuk sebuah domain akan dikirim bersama setiap request ke server, yang dapat sedikit memperlambat koneksi (jika ukurannya besar)

   Session adalah data yang disimpan di sisi server, browser pengguna hanya menyimpan sebuah ID unik.
   - Kelebihan
      1. Data sensitif disimpan di server dan tidak pernah dikirim ke klien, pengguna hanya melihat session ID yang acak.
      2. Karena data disimpan di server, ukurannya bisa jauh lebih besar daripada cookies
      3. Data session dapat disimpan dalam format yang lebih kompleks di server 
   
   - Kekurangan
      1. Setiap session aktif memakan memori di server. 
      2. Session biasanya akan berakhir setelah pengguna tidak aktif selama periode waktu tertentu atau ketika browser ditutup
      3. Jika aplikasi berjalan di beberapa server, diperlukan konfigurasi tambahan

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
   Secara default, penggunaan cookies itu tidak aman, terdapat beberapa resiko potensial dibaliknya, seperti penyerang menyisipkan script berbahaya di sebuah website, yang kemudian bisa mencuri data cookie dari pengguna lain, penyerang menipu browser pengguna yang sedang login di situs A untuk tanpa sadar mengirim request berbahaya ke situs A dari situs B milik penyerang, dan Session Hijacking.

   Django mengatasinya dengan beberapa fitur seperti perlindungan CSRF, di mana setiap form POST harus menyertakan {% csrf_token %} dan Cookie HttpOnly, cookie Session ID Django diatur dengan flag HttpOnly. Ini berarti cookie tersebut tidak dapat diakses melalui JavaScript di browser, secara signifikan mengurangi risiko pencurian cookie melalui serangan XSS.

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
   1. Pertama-tama, saya membuat sebuah fungsi dan form untuk melakukan registrasi pada file views.py, setelah fungsi sudah dibuat, saya membaut halaman html untuk menaimpilkan tampilan register
   2. Setelah semua yang berkaitan dengan register sudah selesai, saya melanjutkan dengan membuat sebuah fungsi login pada file views.py, saya juga membuat html untuk tampilan utama registrasi
   3. Tak lupa saya membaut sebuah fungsi untuk logut, sistem pembuatannya kurang lebih sama yaitu membuat fungsi pada views.py (tidak membuat html)
   4. Dengan adanya fitur registrasi, kita jadi dapat membuat batasan siapa sajakah user yang dapat masuk ke dalam website kita (yang sudah melakukan registrasi), oleh karena itu saya juga membuat sebuah Merestriksi akses halaman dengan menambahkan @login_required(login_url='/login') pada bagian atas dari show_product dan juga main
   5. Setelah semua ini, saya mengakhirinya dengan menghubungkan Product dengan User, yaitu supaya kita dapat melakukan track terhadap user-user yang telah menambahkan produk pada etalase, melakukan filter, dan lain sebagainya