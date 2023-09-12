__1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).__

_Jawab:_

Setep awal, membuat direktori utama bernama ***RushyRushy***. 

Tentunya sebelum mengimplementasikan step pada _checklist_ , pertama-tama melakukan konfigurasi github terlebih dahulu. 

* Pada step ini, melakukan git init dan git config. Git init dilakukan untuk menginisialisasi direktori baru sebagai respositori git. Git config untuk mengatur konfigurasi git. 

Kemudian, membuat repository baru dalam github. 

* Pada step ini, saya membuat repository bernama ***RushyRushy***

Selanjutnya, membuat _README.md_ . 

* Notes: setiap melakukan perubahan selalu diikuti dengan *git add* , *git commit* , dan *git push* .

Step selanjutnya adalah membuat branch baru, disini membuat branch utama yaitu *branch Main* . Dan menghubungkan dengan repositori di github. 

* Menggunakan *git remote* .

Melakukan cloning repository, tujuanya adalah untuk menduplikasi konten ke dalam proyek lokal (kekomputer lokal atau repository hasil cloning). Lalu, melakukan pull pada repository untuk mengambil perubahan dan menggabungkan dengan repositoi lokal.

Selanjutnya membuat branching pada repository, hal ini mempermudah dalam mendevelop aplikasi pada kemudia hari. Karena dengan adanya branching memungkinkan untuk melakukan perubahan pada code tanpa merubah di branch utama.

Kemudian, masuk ke bagian _checklist_:

[x] Membuat sebuah proyek Django baru.

* Menjalankan virual environment. Hal ini agar dapat mengisolasi dependencies dan package dari aplikasi yang sedang di develop.

* Kemudian, pada direktori utama membuat file requirements.txt. Dan tidak lupa untuk install virtual environment.

* Membuat proyek Django baru dengan menggunakan perintah ***django-admin startproject projectname .*** di terminal cmd, dan mengganti ***projectname*** dengan nama ***rushyrushy***.

* 

[x] Membuat aplikasi dengan nama ***main*** pada proyek tersebut.



[x] Melakukan routing pada proyek agar dapat menjalankan aplikasi ***main***.



[x] Membuat model pada aplikasi ***main*** dengan nama ***Item*** dan memiliki atribut wajib sebagai berikut.

* ***name*** sebagai nama item dengan tipe ***CharField***.

- ***amount*** sebagai jumlah item dengan tipe ***IntegerField***.

+ ***description sebagai deskripsi item dengan tipe TextField***.



[x] Membuat sebuah fungsi pada ***views.py*** untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.



[x] Membuat sebuah routing pada ***urls.py*** aplikasi ***main*** untuk memetakan fungsi yang telah dibuat pada ***views.py***.



[x] Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.



[x] Membuat sebuah ***README.md*** yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.



__2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.__

_Jawab:_



__3. Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?__

_Jawab:_

Virtual environment memungkinkan developer untuk membuat lingkungan Python yang terisolasi, di mana setiap proyek dapat memiliki dependensi sendiri-sendiri, terlepas dari dependensi sistem yang ada. Berikut adalah beberapa alasan mengapa kita menggunakan virtual environment:

- Isolasi Dependensi: Setiap proyek Python mungkin memerlukan versi pustaka yang berbeda. Dengan menggunakan virtual environment, developer dapat mengisolasi dependensi ini sehingga perubahan pada satu proyek tidak mempengaruhi proyek lain.

* Menghindari Konflik: Virtual environment membantu menghindari konflik antara library sistem dan library proyek. Misalnya, jika sebuah proyek memerlukan versi library yang berbeda dari yang sudah diinstal di sistem, virtual environment dapat digunakan untuk menginstal versi yang dibutuhkan tanpa mengganggu pustaka sistem.

+ Kemudahan dalam Manajemen Dependensi: Virtual environment memudahkan manajemen dependensi proyek. Developer dapat dengan mudah mengetahui pustaka apa saja yang dibutuhkan oleh proyek dan versi apa yang digunakan.

Namun, developer tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment. Tentunya hal ini memiliki kekurangan, yaitu bisa menimbulkan masalah jika ada konflik antara dependensi Django dan library lain yang sudah terinstal di sistem. Oleh karena itu, penggunaan virtual environment sangat disarankan untuk memastikan bahwa aplikasi Django berjalan dalam environment yang terisolasi dan stabil.

__4. Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.__

_Jawab:_

MVC, MVT, dan MVVM adalah tiga pola arsitektur yang populer dalam pengembangan aplikasi. Pola arsitektur adalah cara untuk mengatur komponen-komponen aplikasi agar lebih mudah dipahami, diuji, dan dimodifikasi. Pola arsitektur ini memiliki tujuan yang sama, yaitu memisahkan logika bisnis (model) dari antarmuka pengguna (view), tetapi memiliki cara yang berbeda untuk melakukannya. Berikut adalah penjelasan singkat dan perbedaan dari ketiga pola arsitektur ini:

* MVC (Model-View-Controller): MVC adalah pola arsitektur yang paling tua dan paling banyak digunakan. MVC membagi aplikasi menjadi tiga komponen utama, yaitu model, view, dan controller. Model adalah komponen yang bertanggung jawab untuk menyimpan dan memproses data serta menerapkan aturan bisnis. View adalah komponen yang bertanggung jawab untuk menampilkan data dari model ke pengguna. Controller adalah komponen yang bertindak sebagai perantara antara model dan view. Controller menerima masukan dari pengguna melalui view, memprosesnya, dan memperbarui model. Kemudian, model memberitahu controller bahwa data telah berubah, dan controller mengirimkan data baru ke view untuk ditampilkan.

- MVT (Model-View-Template): MVT adalah pola arsitektur yang mirip dengan MVC, tetapi menggunakan istilah template sebagai pengganti controller. Template adalah komponen yang berisi kode HTML yang digunakan untuk menghasilkan view. Template dapat menggunakan variabel dan tag khusus untuk menampilkan data dari model. MVT biasanya digunakan dalam framework web seperti Django. Dalam MVT, alur komunikasi antara komponen adalah sebagai berikut: Pengguna mengirimkan permintaan ke server web. Server web meneruskan permintaan ke URL mapper, yang menentukan view mana yang harus dipanggil. View mengambil data dari model dan memberikannya ke template. Template menghasilkan HTML yang dikirim kembali ke view. View mengembalikan HTML sebagai respons ke server web. Server web mengirimkan respons ke pengguna.

+ MVVM (Model-View-ViewModel): MVVM adalah pola arsitektur yang lebih baru dan lebih kompleks daripada MVC dan MVT. MVVM membagi aplikasi menjadi tiga komponen utama, yaitu model, view, dan view model. Model adalah komponen yang sama dengan pada MVC dan MVT, yaitu menyimpan dan memproses data serta menerapkan aturan bisnis. View adalah komponen yang sama dengan pada MVC dan MVT, yaitu menampilkan data dari model ke pengguna. View model adalah komponen yang berfungsi sebagai abstraksi dari view. View model menyediakan properti dan perintah yang dapat diikat oleh view melalui mekanisme yang disebut data binding . Data binding adalah proses otomatis yang menyinkronkan data antara view model dan view tanpa perlu kode tambahan. Dalam MVVM, alur komunikasi antara komponen adalah sebagai berikut: Pengguna melakukan interaksi dengan view. View mengirimkan perintah atau perubahan data ke view model melalui data binding. View model memperbarui model sesuai dengan perintah atau perubahan data tersebut. Model memberitahu view model bahwa data telah berubah. View model mengubah properti atau perintahnya sesuai dengan data baru tersebut. View menerima properti atau perintah baru dari view model melalui data binding dan menampilkan data terbaru ke pengguna.

Perbedaan utama antara ketiga pola arsitektur ini adalah cara mereka mengelola komunikasi antara model dan view. MVC menggunakan controller sebagai perantara, MVT menggunakan template sebagai generator HTML, dan MVVM menggunakan view model sebagai abstraksi dari view. Keuntungan dari MVC adalah mudah dipelajari dan diimplementasikan, keuntungan dari MVT adalah memisahkan logika presentasi dari logika bisnis, dan keuntungan dari MVVM adalah meningkatkan modularitas dan tesabilitas.

