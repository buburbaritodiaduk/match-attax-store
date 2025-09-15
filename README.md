 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
    Data delivery dibutuhkan dalam mengimplementasikan sebuah platform karena ia merupakan sebuah perantara antara suatu sistem dengan sistem lainnya sehingga sistem saling terintegrasi. Tanpa adanya proses data delivery, setiap sistem akan terisolasi dan tidak dapat saling bekerja sama.

 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
    Saya pribadi memilih menggunakan JSON dan menganggap JSON lebih baik karena JSON menggunakan struktur key-value yang mirip dengan JavaScript (menurut saya lebih simpel dibandingkan XML yang basednya HTML). Juga berdasarkan beberapa sumber yang saya baca, JSON memiliki ukuran data yang lebih kecil, mudah dipairsing di hampir semua bahasa, dan ekosistem masa kini mayoritas menggunakan JSON. Sehingga JSON lebih populer jika dibandingkan dengan XML

 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
    is_valid() merupakan sebuah methode otomatis dalam Django dimana ia akan melakukan validasi otomatis terhadap sebuah instruksi field form, seperti tipe data yang dimasukan, max_length, dll. is_valid akan mengembalikan nilai True jika semua valid dan akan mengirimnya ke database.

 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
    csrf_token adalah token unik yang disertakan di setiap form POST. Django akan memverifikasi token ini agar request hanya berasal dari halaman asli. Jika token tidak ada, penyerang bisa membuat halaman palsu yang mengirim request POST ke aplikasi kita dengan cookie korban, kemudian melakukan perintah berbahaya (seperti mengganti password, mengambil data pribadi, dll). Dengan adanya csrf_token, request palsu tidak memiliki token valid sehingga dapat ditolak oleh server.

 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
    1. Pertama-tama saya mendefinisikan struktur data utama di main/models.py, yaitu class Product beserta semua field yang dibutuhkan seperti name, price, description, dll. 
    2. Kemudian, saya membuat logika untuk menampilkan halaman web di main/views.py. Saya membuat fungsi show_main untuk menampilkan semua produk, create_product untuk menangani form penambahan produk baru, dan show_product untuk menampilkan detail satu produk.
    3. Untuk fitur tambah produk, saya membuat form Django di main/forms.py yang terhubung dengan model Product. Di dalam view create_product, saya mengimplementasikan logika untuk memproses form tersebut, termasuk menggunakan if form.is_valid(): untuk validasi data sebelum menyimpannya.
    4. Kemudian, saya membangun UI dengan membuat file-file template HTML (main.html, product_detail.html, dan product_news.html).
    5. Setelah fitur web utama selesai, saya mengimplementasikan fitur data delivery. Saya membuat dua view baru, yaitu show_xml dan show_json, yang mengambil semua data produk lalu mengubahnya (serialisasi) menjadi format XML dan JSON menggunakan django.core.serializers. View ini mengembalikan HttpResponse dengan content_type yang sesuai.   
 
 6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
    Tidak ada, sudah baik.


Screenshot Postman:
1. XML = http://127.0.0.1:8000/xml/
2. JSON = http://127.0.0.1:8000/json/
3. XML_ID = http://127.0.0.1:8000/xml/1/
4. JSON_ID = http://127.0.0.1:8000/json/1/