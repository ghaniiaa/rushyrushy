# Tugas 2: Implementasi Model-View-Template (MVT) pada Django

Ghania Larasati Nurjayadi Putri

2206083003

Kode Asdos: EIA 

Link Adaptable: 

Maaf belum sempat tercopy namun sudah di disabled.

## Jawaban Pertanyaan

__1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).__

_Jawab:_

Step awal, membuat direktori utama bernama ***RushyRushy***. 

Tentunya sebelum mengimplementasikan step pada _checklist_ , pertama-tama melakukan konfigurasi github terlebih dahulu. 

* Pada step ini, melakukan git init dan git config. Git init dilakukan untuk menginisialisasi direktori baru sebagai respositori git. Git config untuk mengatur konfigurasi git. 

Kemudian, membuat repository baru dalam github. 

* Pada step ini, saya membuat repository bernama ***RushyRushy***

Selanjutnya, membuat _README.md_ . 

* Notes: setiap melakukan perubahan selalu diikuti dengan 'git add' , 'git commit' , dan 'git push' .

Step selanjutnya adalah membuat branch baru, disini membuat branch utama yaitu 'branch Main' . Dan menghubungkan dengan repositori di github. 

* Menggunakan 'git remote' .

Melakukan cloning repository, tujuanya adalah untuk menduplikasi konten ke dalam proyek lokal (kekomputer lokal atau repository hasil cloning). Lalu, melakukan pull pada repository untuk mengambil perubahan dan menggabungkan dengan repositoi lokal.

Selanjutnya membuat branching pada repository, hal ini mempermudah dalam mendevelop aplikasi pada kemudian hari. Karena dengan adanya branching memungkinkan untuk melakukan perubahan pada code tanpa merubah di branch utama.

Kemudian, masuk ke bagian _checklist_:

[x] Membuat sebuah proyek Django baru.

* Menjalankan virual environment. Hal ini agar dapat mengisolasi dependencies dan package dari aplikasi yang sedang di develop.

* Kemudian, pada direktori utama membuat file 'requirements.txt'. Dan tidak lupa untuk install virtual environment.

* Membuat proyek Django baru dengan menggunakan perintah 'django-admin startproject projectname'. di terminal cmd, dan mengganti ***projectname*** dengan nama ***rushyrushy***.

* Melakukan konfigurasi proyek dengan menambahkan '[* x *]' pada 'ALLOWED_HOSTS' di 'settings.py' . Hal ini memungkinkan aplikasi dapat diaskses secara luas. 

* Lalu menjalankan server Djanggo, dan melakukan pengecekan apakah web server sudah berjalan. Lalu mengdeactive server.

* Kemudian, membuat file '.gitignore' untuk menentukan file atau direktori mana saja yang bisa diabaikan oleh git.

* Last but not least, mendevelop aplikasi di 'Adatable.io'.

[x] Membuat aplikasi dengan nama ***main*** pada proyek tersebut.

* Setelah terdevelop based untuk aplikasi yang sedang dibangun, langkah selanjutnya kembali menyalakan Virtual Environment.

* Kemudian membuat aplikasi main dalam proyek *RushyRushy*, dengan menjalankan 'python manage.py startapp main'.

[x] Melakukan routing pada proyek agar dapat menjalankan aplikasi ***main***.

* Menambahkan 'main' pada 'INTEALLED_APPS' di settings.py.

* Membuat file baru dengan judul 'main.html' berisikan nilia data yang sesuai dengan yang diinginkan.

[x] Membuat model pada aplikasi ***main*** dengan nama ***Item*** dan memiliki atribut wajib sebagai berikut.

1. 'name' sebagai nama item dengan tipe 'CharField'.

1. 'amount' sebagai jumlah item dengan tipe 'IntegerField'.

1. 'description' sebagai deskripsi item dengan tipe 'TextField'.

* Membuka 'models.py' dan memberikan inisiasi dan deskripsi model dalam Djanggo.
'''
	name = models.CharField(max_length=255)
	
	date_added = models.DateField(auto_now_add=True)

	amount = models.IntegerField()

	description = models.TextField()

	category = models.TextField()

	price = models.IntegerField()
'''

* Menjalankan migrasi model untuk melacak perubaham pada data base. 

[x] Membuat sebuah fungsi pada 'views.py' untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

* Pada step ini, akan menghubungkan view dan template. 

* Melakuakn adjust pada file 'views.py'. Pada file terebut melakukan _render_ untuk merender tampilan HTML dan juga pada step ini akan dilakukan pengimporan fungsi dari modul 'django.shortcuts' . 

* Kemudian menambahkan fungsi 'show_main' yang berisikan data yang akan dikirimkan ke interface. Pada context ini, sesuai dengan permintaan pada _checklist_ point yaitu, **Nama Company**, **Nama**, dan **Kelas**.

* Pada fungsi, terdapat 'return render' untuk merender interface 'main.html'. 

* Selanjutnya, memodifikasi template 'main.html'
'''

	<h1>RushyRushy</h1>

	<h5>Name: </h5>

	<p>{{name}}</p>

	<h5>Class: </h5>

	<p>{{class}}</p> 
'''

[x] Membuat sebuah routing pada ***urls.py*** aplikasi ***main*** untuk memetakan fungsi yang telah dibuat pada ***views.py***.

* Sebelum melakukan routing, tentu perlua dibuatnya 'urls.py' pada direktori main. File terebut digunakan untuk mengatur rute URL spesifik pad aplikasi. --> URLS APLIKASI

* Kemudian, membuka 'urls.py' pada direktori proyek dan menambahkan fungsi include serta membuat rute tambahan yang mengarah pada tampilan main. Hal ini dilakukan untuk mengatur rute pada tingkat proyek dan mengimpor rute-rute aplikasi. --> URLS PROYEK

* Selanjutnya menjalankan perintah 'python manage.py runserver' dan melakukan pengecekan dengan **http://localhost:8000/main/** apakah web sudah berhasil dibuat.

* Terakhir, membuat unit testing. 

[x] Melakukan deployment ke Adaptable terhadap aplikasi yang sudah dibuat sehingga nantinya dapat diakses oleh teman-temanmu melalui Internet.

* Melakukan pengecekan kembali pada adaptable yang telah didevelop untuk aplikasi RushyRushy.

[x] Membuat sebuah ***README.md*** yang berisi tautan menuju aplikasi Adaptable yang sudah di-deploy, serta jawaban dari beberapa pertanyaan berikut.

* Meletakan link akses untuk membuka aplikasi dan menjawab pertanayan-pertanyaan yang terlampir pada _checklist_ . 


__2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.__

_Jawab:_

![CLIENT (USER)](https://github.com/ghaniiaa/rushyrushy/assets/116947086/bc39eb84-a9ae-475b-9ec1-29abbd1d2dee)

_Notes_:

* urls.py: Ketika client membuat request ke server Django, Django pertama kali mencocokkan URL yang diminta dengan pola URL yang didefinisikan dalam file urls.py. File ini bertindak sebagai pengendali lalu lintas, mengarahkan request ke fungsi view yang sesuai.

* views.py: Fungsi view dalam views.py bertindak sebagai controller yang mengendalikan alur aplikasi. Fungsi view menerima request HTTP, melakukan operasi yang diperlukan, dan mengembalikan respons HTTP. Fungsi view dapat berinteraksi dengan model dan template.

* models.py: Model dalam models.py mendefinisikan struktur data aplikasi. Model adalah representasi dari tabel database dan mereka digunakan untuk berinteraksi dengan database. Fungsi view dapat meminta data dari model, dan model akan mengambil data dari database dan mengembalikannya ke fungsi view.

* Template (HTML): Template adalah file HTML yang digunakan untuk merender tampilan halaman web. Fungsi view merender template dengan konteks, yaitu variabel-variabel yang dapat digunakan dalam template. Template kemudian dikembalikan sebagai respons HTTP ke client.

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

