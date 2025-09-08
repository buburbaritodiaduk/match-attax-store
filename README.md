https://aryandana-pascua-matchattaxstore.pbp.cs.ui.ac.id/

1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Cara saya mengimplementasikan checklist di atas:
    - Pertama-tama, saya membuat Git khusus untuk projek ini, kemudian saya melakukan git clone untuk mendapatkan folder repo nya
    - Setelah mendapatkan folder repo, saya membuat virtual environment, menambahkan serta mendownload dependencies, dan membuat projek Djangonya
    - Saya juga menambahkan beberapa kebutuhan seperti env. prod. dan juga beberapa settings tambahan pada settings.py
    - Selanjutnya, saya membuat aplikasi main dalam projek saya serta melakukan beberapa adjust pada settings.py dan models.py agar projek Django saya dapat berjalan
    - Saya juga membuat sebuah fungsi show_main supaya dapat mengembalikan parameter request. pada views.py dan juga class baru pada models.py dengan nama Product yang mempunyai beberapa atribut sesuai kebutuhan tugas ini
    - Terakhir saya melakukan deployment ke PWS 

2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
    Bagan
             a            
    - Client -> URLS 
                   |b   
             c     v   e
      Model <-> Views -> HTTP Response
                  ^
                  |d
               Template

    - a: Django akan melakukan pengecekan pada urls.py setelah user mengakses alamat
    - b: views.py akan berfungsi sebagai perantara, jika user membutuhkan database, maka views akan memanggil model.py
    - c: views dapat melakukan read/write pada model.py sesuai dengan kebutuhan yang diperlukan oleh user
    - d: data yang telah dioleh pada views.py akan  dikirim kepada template dan template akan menampilkan interface HTML (render)
    - e: HTML yang telah dirender, hasilnya akan dikembalikan kepada user sebagai HTTP Response

3. Jelaskan peran settings.py dalam proyek Django!
    - Mengacu pada sumber yang saya baca, settings.py berperan penting dalam mengatur semua komponen yang ada pada projek Django, seperti URL, views, models, templates, dll. settings dapat mengatur jenis database apa yang dipakai, menyimpan routing utama yang dipakai, menentukan di mana file html template disimpan, dan masih banyak lagii.

4. Bagaimana cara kerja migrasi database di Django?
Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
    - Cara untuk melakukan migrasi database di Django adalah dengan mengaktifkan env lalu menggenerate migrasi dengan menulis python manage.py makemigrations pada cmd dan melakukan apply migrasi ke database dengan cara menulis python manage.py migrate.
    - Menurut saya, dengan struktur MVT yang dimiliki oleh Django, saya pribadi sangat dengan mudah memahami bagaimana cara kerja database, html, dll berjalan berkaitan satu sama lain, jika dibandingkan dengan framework lainnya seperti Ruby yang menuntut usernya untuk mengikuti aturan-aturan mereka, Django lebih mengajarkan kita bagaimana cara kerja dari software itu sendiri.  

5. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
    - Sudah baik
