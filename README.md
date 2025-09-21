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

   Autentikasi: 
 
3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?

4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?

5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).