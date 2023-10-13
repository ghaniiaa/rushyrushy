Ghania Larasati Nurjayadi Putri

2206083003

Kode Asdos: EIA 

# Tugas 2: Implementasi Model-View-Template (MVT) pada Django

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

* Notes: setiap melakukan perubahan selalu diikuti dengan `git add` , `git commit` , dan `git push` .

Step selanjutnya adalah membuat branch baru, disini membuat branch utama yaitu `branch Main` . Dan menghubungkan dengan repositori di github. 

* Menggunakan `git remote add origin <URL_REPO>` .

Melakukan cloning repository `git clone <URL_CLONE>`, tujuannya adalah untuk menduplikasi konten ke dalam proyek lokal (kekomputer lokal atau repository hasil cloning). Lalu, melakukan pull pada repository untuk mengambil perubahan dan menggabungkan dengan repositoi lokal.

Selanjutnya membuat branching pada repository, hal ini mempermudah dalam mendevelop aplikasi pada kemudian hari. Karena dengan adanya branching memungkinkan untuk melakukan perubahan pada code tanpa merubah di branch utama. Kemudian, melakukan **Compare & pull request** dan **Merge pull request** pada github.

Kemudian, masuk ke bagian _checklist_:

[x] Membuat sebuah proyek Django baru.

* Menjalankan virual environment (`python -m venv env` -> `env\Scripts\activate.bat`). Hal ini agar dapat mengisolasi dependencies dan package dari aplikasi yang sedang di develop.

_notes: cara mematikan virtual environment dengan `deactivate`_

* Kemudian, pada direktori utama membuat file `requirements.txt`. Dan tidak lupa untuk install virtual environment.

* Membuat proyek Django baru dengan menggunakan perintah `django-admin startproject projectname`. di terminal cmd, dan mengganti ***projectname*** dengan nama ***rushyrushy***.

* Melakukan konfigurasi proyek dengan menambahkan `[* x *]` pada `ALLOWED_HOSTS` di `settings.py` . Hal ini memungkinkan aplikasi dapat diaskses secara luas. 

* Lalu menjalankan server Djanggo, dan melakukan pengecekan apakah web server sudah berjalan. Lalu mengdeactive server.

* Kemudian, membuat file `.gitignore` untuk menentukan file atau direktori mana saja yang bisa diabaikan oleh git.

* Last but not least, mendevelop aplikasi di `Adatable.io`.

[x] Membuat aplikasi dengan nama ***main*** pada proyek tersebut.

* Setelah terdevelop based untuk aplikasi yang sedang dibangun, langkah selanjutnya kembali menyalakan Virtual Environment.

* Kemudian membuat aplikasi main dalam proyek *RushyRushy*, dengan menjalankan `python manage.py startapp main`.

[x] Melakukan routing pada proyek agar dapat menjalankan aplikasi ***main***.

* Menambahkan `main` pada `INTALLED_APPS` di `settings.py`.

* Membuat file baru dengan judul `main.html` berisikan nilia data yang sesuai dengan yang diinginkan.

[x] Membuat model pada aplikasi ***main*** dengan nama ***Item*** dan memiliki atribut wajib sebagai berikut.

1. `name` sebagai nama item dengan tipe `CharField`.

1. `amount` sebagai jumlah item dengan tipe `IntegerField`.

1. `description` sebagai deskripsi item dengan tipe `TextField`.

* Membuka `models.py` dan memberikan inisiasi dan deskripsi model dalam Djanggo.

```

name = models.CharField(max_length=255)
date_added = models.DateField(auto_now_add=True)
amount = models.IntegerField()
description = models.TextField()
category = models.TextField()
price = models.IntegerField()

```

* Menjalankan migrasi model untuk melacak perubaham pada data base. 

[x] Membuat sebuah fungsi pada `views.py` untuk dikembalikan ke dalam sebuah template HTML yang menampilkan nama aplikasi serta nama dan kelas kamu.

* Pada step ini, akan menghubungkan view dan template. 

* Melakuakn adjust pada file `views.py`. Pada file terebut melakukan _render_ untuk merender tampilan HTML dan juga pada step ini akan dilakukan pengimporan fungsi dari modul `django.shortcuts` . 

* Kemudian menambahkan fungsi `show_main` yang berisikan data yang akan dikirimkan ke interface. Pada context ini, sesuai dengan permintaan pada _checklist_ point yaitu, **Nama Company**, **Nama**, dan **Kelas**.

* Pada fungsi, terdapat `return render` untuk merender interface `main.html`. 

* Selanjutnya, memodifikasi template `main.html`

```

	<h1>RushyRushy</h1>
	<h5>Name: </h5>
	<p>{{name}}</p>
	<h5>Class: </h5>
	<p>{{class}}</p> 

```

[x] Membuat sebuah routing pada ***urls.py*** aplikasi ***main*** untuk memetakan fungsi yang telah dibuat pada ***views.py***.

* Sebelum melakukan routing, tentu perlua dibuatnya `urls.py` pada direktori main. File terebut digunakan untuk mengatur rute URL spesifik pad aplikasi. --> URLS APLIKASI

* Kemudian, membuka `urls.py` pada direktori proyek dan menambahkan fungsi include serta membuat rute tambahan yang mengarah pada tampilan main. Hal ini dilakukan untuk mengatur rute pada tingkat proyek dan mengimpor rute-rute aplikasi. --> URLS PROYEK

* Selanjutnya menjalankan perintah `python manage.py runserver` dan melakukan pengecekan dengan **http://localhost:8000/main/** apakah web sudah berhasil dibuat.

* Terakhir, membuat unit testing. 

```

from django.test import TestCase, Client
from .models import Product

class MainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/main/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/main/')
        self.assertTemplateUsed(response, 'main.html')

    def test_main_contains_name(self):
        response = Client().get('/main/')
        self.assertContains(response, 'Ghania Larasati Nurjayadi Putri')

    def test_main_contains_class(self):
        response = Client().get('/main/')
        self.assertContains(response, 'PBP D')

    def test_main_template_context(self):
        response = Client().get('/main/')
        self.assertEqual(response.context['name'], 'Ghania Larasati Nurjayadi Putri')
        self.assertEqual(response.context['class'], 'PBP D')

class ProductTestCase(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            amount=10,
            description='This is a test product',
            category='Test Category',
            price=100
        )

    def test_product_creation(self):
        product = Product.objects.get(name='Test Product')
        self.assertEqual(product.amount, 10)
        self.assertEqual(product.description, 'This is a test product')
        self.assertEqual(product.category, 'Test Category')
        self.assertEqual(product.price, 100)

    def test_product_string_representation(self):
        self.assertEqual(str(self.product), 'Test Product')

    def test_product_date_added_auto_now_add(self):
        self.assertIsNotNone(self.product.date_added)


```

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


# Tugas 3: Implementasi Form dan Data Delivery pada Django

## Jawaban Pertanyaan

__1. Apa perbedaan antara form POST dan form GET dalam Django?__

_Jawab:_ 

* **Form POST** : Form Post digunakan untuk mengirimkan data ke server tanpa menampilkan data tersebut   di URL. Data yang dikirimkan sebagai merupakan bagian dari permintaan HTTP dan tidak terlihat oleh pengguna. Form Post adalah metode yang cocok digunakan dalam mengirimkan data sensitif (contoh: kata sandi atau informasi pribadi).

* **Form GET** : Form GET digunakan untuk  mengirim data melalui URL sebagai query string. Data dapat dilihat oleh pengguna di URL, dan permintaan GET idealnya digunakan untuk permintaan pencarian atau permintaan yang tidak mengubah status server. Metode ini memiliki keterbatasan panjang URL yang dapat dikirim.

**Perbedaan POST dan GET**

1. Form POST tidak menampilkan nilai variabel di URL, sedangkan form GET menampilkan nilai variabel di URL sehingga user dapat dengan mudah memasukkan nilai variabel baru.

1. Form POST lebih aman daripada form GET.

1. Form POST tidak dibatasi panjang string, sedangkan form GET dibatasi panjang string sampai 2047 karakter.

__2. Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?__

_Jawab:_

+ **XML** *(eXtensible Markup Language)* : format teks yang digunakan untuk merepresentasikan data dalam struktur hirarkis. Ia sangat serbaguna dan dapat digunakan untuk merepresentasikan berbagai jenis data. Namun, XML memiliki sintaks yang lebih kompleks dan seringkali menghasilkan dokumen yang lebih besar dibandingkan JSON.

+ **JSON** *(JavaScript Object Notation)* : format teks yang digunakan untuk pertukaran data ringan. Ia biasanya lebih mudah dibaca oleh manusia dibandingkan XML karena memiliki sintaks yang sederhana. JSON umumnya digunakan dalam aplikasi web modern dan layanan web RESTful karena ukuran data yang lebih kecil dan parsing yang lebih cepat.

+ **HTML** *(HyperText Markup Language)* : bahasa markup yang digunakan untuk membuat halaman web. Ia berfokus pada tampilan dan struktur halaman web dan tidak dirancang untuk pertukaran data. Namun, HTML juga bisa digunakan untuk mengirim data melalui form dalam elemen-elemen seperti <input>.

__3. Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?__
 
_Jawab:_

1. JSON mendukung semua browser dan sebagian besar bahasa pemrograman modern, sehingga data dalam format JSON dapat dengan mudah diolah dan dimanipulasi di berbagai platform dan lingkungan.

1. JSON memiliki struktur data yang intuitif dan konsisten, sehingga data dapat direpresentasikan dengan fleksibel dan kompleks, seperti objek dalam objek atau array dari objek-objek.

1. JSON memiliki sintaks yang mudah dibaca oleh manusia, sehingga memudahkan pengembang dalam memahami dan menganalisis data selama proses pengembangan dan debugging.

1. JSON memiliki format yang ringan dan terstruktur, sehingga data dapat dikirim dengan cepat melalui jaringan dan diurai dengan mudah oleh klien.

__4. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).__

_Jawab:_

Step awal sebelum mengerjakan `checklist`:

* Mengatur routing dari `main/` ke `/`
Pada step ini mengubah isi `urls.py`, dimana mengubah bagian `urlpatterns` dengan mengubah routing `main/` ke `/`.

* Kemudian melakukan implementasi Skeleton
    
    * Pada step ini, membuat folder baru yaitu folder `template` dan membuat berkas `base.html`.
    
    * Lalu melakukan penyesuaian `settings.py` pada subdirektori.
    
    * Dan terkahir membuat `main.html` pada subdirektori `templates` di direktori `main`.

_Checklist :_
+ Membuat input `form`
    *  Step pertama adalah membuat file `forms.py` pada direktori `main`.
    ```
    from django.forms import ModelForm
    from main.models import Product

    class ProductForm(ModelForm):
        class Meta:
            model = Product
            fields = ["name", "amount", "description", "category", "price"]
    ```

    * Menambahkan `import` pada `views.py` di `main`
    ```
    from django.http import HttpResponseRedirect
    from main.forms import ProductForm
    from django.urls import reverse
    from .models import Product
    ```

    * Kemudian, menambahkan fungsi baru pada `views.py` di `main`
    ```
    def show_main(request):
    products = Product.objects.all()
    total_items = products.count()  # Menghitung jumlah item yang tersimpan

    context = {
        'name': 'Ghania Larasati Nurjayadi Putri',  # Ganti dengan nama kamu
        'class': 'PBP D',  # Ganti dengan kelas kamu
        'products': products,
        'total_items': total_items,  # Menyertakan jumlah item
    }

    return render(request, "main.html", context)

    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "create_product.html", context)
    ```

    * Selanjutnya, mengimport fungsi dari `views.py` ke `urls.py` pada direktori `main`
    ```
    from main.views import show_main, create_product
    ```

    * Lalu tambahkan `path` baru pada `urlpatterns` di `urls.py`
    ```
    path('create-product', create_product, name='create_product'),
    ```

    * Membuat `create_product.html` pada direktori `main` dan di subdirektori `templates`, yang berisi
    ```
    {% extends 'base.html' %} 

        {% block content %}
        <h1>Add New Product</h1>

        <form method="POST">
            {% csrf_token %}
            <table>
                {{ form.as_table }}
                <tr>
                    <td></td>
                    <td>
                        <input type="submit" value="Add Product"/>
                    </td>
                </tr>
            </table>
        </form>

    {% endblock %}
    ```

    * Kemudian men-adjust `main.html`
    ```
    {% extends 'base.html' %}

    {% block content %}
        <h1>RushyRushy</h1>

        <h5>Name:</h5>
        <p>{{name}}</p>

        <h5>Class:</h5>
        <p>{{class}}</p>

    <!-- Menampilkan pesan jumlah item yang tersimpan -->
    <p>Kamu menyimpan {{ total_items }} item pada aplikasi ini.</p>

    <table>
        <tr>
            <th>Name</th>
            <th>Date Added</th>
            <th>Amount</th>
            <th>Description</th>
        <th>Category</th>
            <th>Price</th>
        </tr>

        {% comment %} Berikut cara memperlihatkan data produk di bawah baris ini {% endcomment %}

        {% for product in products %}
            <tr>
                <td>{{product.name}}</td>
            <td>{{product.date_added}}</td>
            <td>{{product.amount}}</td>
                <td>{{product.description}}</td>
                <td>{{product.category}}</td>
                <td>{{product.price}}</td>
            </tr>
        {% endfor %}
    </table>

    <br />

    <a href="{% url 'main:create_product' %}">
        <button>
            Add New Product
        </button>
    </a>

    {% endblock content %}
    ```

+ Menambahkan 5 fungsi `views` (HTML, XML, JSON, XML by ID, dan JSON by ID)

    * Menampilkan form yang telah dibuat dengan menggunakan template HTML pada `views,py` 
    ```
    def show_main(request):
        products = Product.objects.all()
        total_items = products.count()  # Menghitung jumlah item yang tersimpan

        context = {
            'name': 'Ghania Larasati Nurjayadi Putri',  # Ganti dengan nama kamu
            'class': 'PBP D',  # Ganti dengan kelas kamu
            'products': products,
            'total_items': total_items,  # Menyertakan jumlah item
        }

        return render(request, "main.html", context)
    
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            form.save()
            return HttpResponseRedirect(reverse('main:show_main'))

        context = {'form': form}
        return render(request, "create_product.html", context)
    ```

    Kemudian sebelum melakukan `views` untuk XML, JSON, XML by ID, dan JSON by ID:

    Mengimport pada `views.py`,
    ```
    from django.http import HttpResponse
    from django.core import serializers
    ```

    * Menampilkan form yang telah dibuat dengan menggunakan template XML pada `views,py`
    ```
    def show_xml(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```

    * Menampilkan form yang telah dibuat dengan menggunakan template JSON pada `views,py`
    ```
    def show_json(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

    * Menampilkan form yang telah dibuat dengan menggunakan template XML by ID pada `views,py`
    ```
    def show_xml_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")
    ```

    * Menampilkan form yang telah dibuat dengan menggunakan template JSON by ID pada `views,py`
    ```
    def show_json_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```

+ Membuat routing URL untuk masing-masing `views`

    * Menampilkan form yang telah dibuat dengan menggunakan template HTML

        - Import pada `urls.py`
        ```
        from main.views import show_main, create_product
        ```

        - Menambahkan `path` pada `urls.py`
        ```
        path('create-product', create_product, name='create_product'),
        ```

    * Menampilkan form yang telah dibuat dengan menggunakan template XML

        - Import pada `urls.py`
        ```
        from main.views import show_main, create_product, show_xml 
        ```

        - Menambahkan `path` pada `urls.py`
        ```
        path('xml/', show_xml, name='show_xml'), 
        ```

    * Menampilkan form yang telah dibuat dengan menggunakan template JSON

        - Import pada `urls.py`
        ```
        from main.views import show_main, create_product, show_xml, show_json
        ```

        - Menambahkan `path` pada `urls.py`
        ```
        path('json/', show_json, name='show_json'), 
        ```

    * Menampilkan form yang telah dibuat dengan menggunakan template XML by ID

        - Import pada `urls.py`
        ```
        from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id
        ```

        - Menambahkan `path` pada `urls.py`
        ```
        path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
        ```

    * Menampilkan form yang telah dibuat dengan menggunakan template JASN by ID

        - Import pada `urls.py`
        ```
        from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id 
        ```

        - Menambahkan `path` pada `urls.py`
        ```
        path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
        ```

+ Menjawab pada `READ.ME`

    Menjawab README.md sesuai dengan jawaban diatas.

+ Mengakses URL dengan Postman

    1. Mendownload `Postman`

    1. Memasukan link ke dalam `Postman` dan melakukan `send`:

        * **HTML** : `http://localhost:8000/`

        * **XML** : `http://localhost:8000/xml`

        * **JSON** : ` http://localhost:8000/json`

        * **XML by ID** : `http://localhost:8000/xml/[id]`

        * **JSON by ID** : `http://localhost:8000/json/[id]`

+ Melakukan `add -commit -push` ke GitHub

    Tidak lupa melakukan `add -commit -push` pada terminal untuk menyimpan semua perubahan.

## POSTMAN

* *HTML*

![image](https://github.com/ghaniiaa/rushyrushy/assets/116947086/8050542c-292d-4665-98a6-7cc2fedc1e62)

+ *XML*

![image](https://github.com/ghaniiaa/rushyrushy/assets/116947086/b9e397ba-9c2d-4f3d-a895-0ee3666a04eb)

- *JSON*

![image](https://github.com/ghaniiaa/rushyrushy/assets/116947086/56861f59-0111-4dda-b239-8648efeb29db)

+ *XML by ID*

![image](https://github.com/ghaniiaa/rushyrushy/assets/116947086/188a9387-b91e-424f-a81d-dde1b1ce370a)

- *JSON by ID*

![image](https://github.com/ghaniiaa/rushyrushy/assets/116947086/1895462a-5dea-41f8-97ad-bc7671b6ec1e)


# Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django

## Jawaban Pertanyaan

__1. Apa itu Django `UserCreationForm`, dan jelaskan apa kelebihan dan kekurangannya?__

_Jawab:_ 

Django `UserChangeForm` adalah sebuah kelas yang diturunkan dari `django.contrib.auth.forms` dan digunakan untuk membuat formulir pendaftaran pengguna baru. 

* Kelebihan dari `UserChangeForm`: 

    * Mudah Digunakan: `UserChangeForm` sudah tersedia dan siap digunakan dalam Django, sehingga Anda tidak perlu membuatnya dari awal.

    * Validasi Bawaan: Form ini mencakup validasi bawaan untuk memastikan bahwa data yang dimasukkan oleh pengguna memenuhi persyaratan yang ditetapkan, seperti panjang password, dan username yang unik.

    * Integrasi Mudah: `UserChangeForm` terintegrasi dengan baik dengan sistem autentikasi Django, sehingga memudahkan Anda dalam mengelola akun pengguna.

* Kekurangannya dari `UserChangeForm`: 
    * Hanya memiliki dua bidang, yaitu username dan password, sehingga jika ingin menambahkan bidang lain seperti email, nama, atau profil, harus membuat kelas turunan sendiri atau menggunakan kelas lain seperti `UserChangeForm` atau `UserCreationForm`.

    * Tidak Otomatis Mengelola Semua Aspek Keamanan: `UserCreationForm` membantu dalam membuat akun pengguna, tetapi tidak menangani semua aspek keamanan, seperti melindungi terhadap serangan brute force atau SQL injection. Maka perlu mengambil langkah-langkah tambahan untuk menjaga keamanan aplikasi.


__2. Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?__

_Jawab:_ 

Dalam konteks Django:

* Autentikasi adalah proses verifikasi identitas pengguna, yaitu memeriksa apakah pengguna yang mengakses aplikasi adalah orang yang ia klaim sebagai identitasnya. Django menyediakan sistem autentikasi yang mencakup pengelolaan akun pengguna, otentikasi melalui username dan password, serta dukungan untuk autentikasi dengan OAuth, token, atau metode lainnya.

* Otorisasi adalah proses menentukan izin atau hak akses apa yang diberikan kepada pengguna setelah mereka berhasil terotentikasi. Ini melibatkan pengelolaan tingkat akses, seperti apa yang bisa dilakukan atau diakses oleh pengguna dalam aplikasi.

Keduanya penting karena autentikasi memastikan bahwa hanya pengguna yang sah yang dapat mengakses aplikasi, sementara otorisasi mengendalikan apa yang dapat dilakukan oleh pengguna yang telah terotentikasi.

__3. Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?__

_Jawab:_ 

Cookies adalah file teks kecil yang disimpan oleh browser web di komputer pengguna, yang berisi informasi tentang pengguna dan preferensinya saat mengunjungi sebuah situs web. Django menggunakan cookies untuk mengelola data sesi pengguna, yaitu data yang berlaku selama pengguna mengakses aplikasi web dalam satu browser. Data sesi dapat berisi informasi seperti identitas pengguna, status login, bahasa, tema, keranjang belanja, dan lain-lain. Django menyimpan data sesi di server dan mengirimkan sebuah cookie dengan ID sesi ke browser pengguna. Cookie ini kemudian dikirim kembali ke server setiap kali pengguna membuat permintaan, sehingga server dapat mengambil data sesi yang sesuai dengan ID sesi tersebut.

__4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?__

_Jawab:_ 

Penggunaan cookies tidak sepenuhnya aman secara default dalam pengembangan web, karena ada risiko potensial yang harus diwaspadai, seperti:

* Cookie dapat dicuri oleh pihak ketiga yang dapat mengakses jaringan yang sama dengan pengguna, misalnya melalui serangan man-in-the-middle atau sniffing. Hal ini dapat menyebabkan pencurian identitas, pembajakan sesi, atau penyalahgunaan data pribadi pengguna. Untuk mencegah hal ini, sebaiknya menggunakan protokol HTTPS yang mengenkripsi komunikasi antara browser dan server, serta mengatur atribut secure pada cookie agar hanya dikirim melalui HTTPS.

* Cookie dapat dimodifikasi oleh pengguna atau skrip jahat yang berjalan di browser, misalnya melalui serangan cross-site scripting (XSS) atau tampering. Hal ini dapat menyebabkan pemalsuan permintaan, manipulasi data, atau eksekusi kode jahat di server. Untuk mencegah hal ini, sebaiknya menggunakan mekanisme validasi dan verifikasi pada cookie, seperti tanda tangan digital, checksum, atau token CSRF, serta mengatur atribut httponly pada cookie agar tidak dapat diakses oleh skrip JavaScript.

* Cookie dapat melanggar privasi pengguna jika mengandung informasi sensitif atau pribadi yang tidak diinginkan oleh pengguna, misalnya melalui pelacakan, profil, atau iklan yang ditargetkan. Hal ini dapat menyebabkan ketidaknyamanan, ketidakpercayaan, atau kerugian bagi pengguna. Untuk mencegah hal ini, sebaiknya menggunakan cookie sesuai dengan hukum dan etika yang berlaku, seperti meminta persetujuan pengguna, memberikan pilihan opt-out, atau menghapus cookie yang sudah tidak diperlukan.

__5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).__

_Jawab:_ 

Berikut adalah langkah-langkah implementasi dari checklist yang telah disebutkan sebelumnya:

***Implementasi Autentikasi, Session, dan Cookies:***

+ **Aktivasi Virtual Environment**: Aktifkan virtual environment dengan menjalankan perintah berikut di direktori proyek Anda:

    ```
    env\Scripts\activate.bat
    ```

+ **Membuat Formulir Pendaftaran**: 

    Di `views.py`, tambahkan import dan buat fungsi `register` yang akan menangani formulir pendaftaran:

    ```
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib import messages

    def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form': form}
        return render(request, 'register.html', context)
    ```

+ **Membuat Halaman Registrasi**: 
    
    Buat template HTML dengan nama `register.html` untuk halaman registrasi yang akan menampilkan formulir pendaftaran dan pesan kesalahan jika ada kesalahan dalam pengisian formulir.

+ **Membuat Fungsi Login**: 

    Di `views.py`, tambahkan import dan buat fungsi `login_user` yang akan menangani proses login:

    ```
    from django.contrib.auth import authenticate, login

    def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('main:show_main')
            else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
        context = {}
        return render(request, 'login.html', context)
    ```

+ **Membuat Halaman Login**: 

    Buat template HTML dengan nama `login.html` untuk halaman login yang akan menampilkan formulir login dan pesan kesalahan jika diperlukan.

+ **Membuat Tombol Logout**: 
    
    Di `views.py`, tambahkan fungsi `logout_user` untuk mengelola proses logout:

    ```
    from django.contrib.auth import logout

    def logout_user(request):
        logout(request)
        return redirect('main:login')
    ```

+_ **Membatasi Akses**: 

    Terapkan pembatasan akses dengan decorator `@login_required` di halaman utama:

    ```
    from django.contrib.auth.decorators import login_required

    @login_required(login_url='/login')
    def show_main(request):
        # Konten halaman utama
    ```

+ **Menggunakan Cookies**: 

Di `views.py`, tambahkan kode untuk melacak aktivitas login terakhir pengguna:

    ```
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse

    def login_user(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                response = HttpResponseRedirect(reverse("main:show_main"))
                response.set_cookie('last_login', str(datetime.datetime.now()))
                return response
            else:
                messages.info(request, 'Sorry, incorrect username or password. Please try again.')
        context = {}
        return render(request, 'login.html', context)
    ```

    Di dalam `show_main`, tambahkan informasi aktivitas login terakhir ke dalam variabel `context`:

    ```
    context = {
        'name': request.user.username,
        'class': 'PBP A',
        'products': products,
        'last_login': request.COOKIES['last_login'],
    }
    ```

    Dan tambahkan kode di halaman HTML `main.html` untuk menampilkan informasi tersebut.

+ **Menghubungkan Produk dengan Pengguna**: 

    Di model `Product` dalam `models.py`, hubungkan setiap produk dengan pengguna yang membuatnya:

    ```
    from django.contrib.auth.models import User

    class Product(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        # Sisanya adalah field lainnya
    ```

    Di `views.py`, dalam fungsi `create_product`, tambahkan informasi pengguna sebelum menyimpan produk:

    ```
    def create_product(request):
        form = ProductForm(request.POST or None)

        if form.is_valid() and request.method == "POST":
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return HttpResponseRedirect(reverse('main:show_main'))
    ```

+ **Migrasi Basis Data**: 

    Jalankan migrasi basis data untuk menerapkan perubahan dalam model produk dengan perintah:

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

    Saat migrasi dilakukan, mungkin Anda harus memilih opsi untuk menetapkan nilai default untuk field `user` pada seluruh baris yang sudah ada dalam basis data.

+  **Menjalankan Aplikasi**: 

    Jalankan aplikasi Django Anda dengan perintah:

    ```
    python manage.py runserver
    ```

    Selanjutnya, buka http://localhost:8000/ di browser Anda dan uji coba registrasi, login, logout, dan tampilan halaman utama dengan baik.


***Mengimplementasikan Penambahan dan Pengurangan Amount:***

    + **Tambahkan Kolom Stock pada Model Product:**
    
        - Buka file `models.py` dalam aplikasi Django Anda.

        - Tambahkan kolom `stock` ke dalam model `Product` untuk melacak jumlah stok suatu produk.

    ```
    class Product(models.Model):
        # Kolom-kolom yang ada sebelumnya
        stock = models.IntegerField(default=0)  # Tambahkan kolom stock
    ```

    + **Migrasi Basis Data:**

        - Jalankan perintah `makemigrations` dan `migrate` untuk membuat dan menerapkan perubahan basis data baru.

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```

    + **Update Tampilan HTML:**

        - Buka file `main.html` atau template yang Anda gunakan untuk menampilkan produk.

        - Tambahkan tombol "+" dan "-" di samping kolom amount untuk setiap produk.

    ```
    <td>
        <form method="POST" action="{% url 'main:decrement_stock' product.id %}">
            {% csrf_token %}
            <button type="submit" class="btn btn-sm btn-danger">-</button>
        </form>
        <span class="mx-2">{{ product.amount }}</span>
        <form method="POST" action="{% url 'main:increment_stock' product.id %}">
            {% csrf_token %}
            <button type="submit" class="btn btn-sm btn-success">+</button>
        </form>
    </td>
    ```

    + **Membuat Fungsi View Untuk Penambahan dan Pengurangan Stock:**
    
        - Buka file `views.py` dan tambahkan fungsi view `increment_stock` dan `decrement_stock` untuk menangani permintaan pengguna ketika mereka mengklik tombol "+" atau "-".

    ```
    from django.shortcuts import get_object_or_404

    @login_required(login_url='/login')
    def increment_stock(request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        if request.method == 'POST':
            product.stock += 1
            product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    @login_required(login_url='/login')
    def decrement_stock(request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        if request.method == 'POST':
            if product.stock > 0:
                product.stock -= 1
                product.save()
        return HttpResponseRedirect(reverse('main:show_main'))
    ```

    + **Tambahkan URL untuk Fungsi View Baru:**

        - Buka file `urls.py` dalam aplikasi Anda dan tambahkan URL untuk view `increment_stock` dan `decrement_stock`.

    ```
    urlpatterns = [
        # URL lainnya
        path('increment_stock/<int:product_id>/', views.increment_stock, name='increment_stock'),
        path('decrement_stock/<int:product_id>/', views.decrement_stock, name='decrement_stock'),
    ]
    ```

    + **Terapkan Perubahan di Template:**

        - Pastikan perubahan HTML di template Anda sudah sesuai dengan langkah-langkah di atas.

    + **Uji Coba**: 
    
    Jalankan server Django Anda (`python manage.py runserver`) dan uji coba fitur penambahan dan pengurangan amount pada produk.

***Mengimplementasikan Penghapusan Objek:***

    + **Tambahkan Tombol Hapus di Tampilan HTML:**

        - Buka file `main.html` atau template yang Anda gunakan untuk menampilkan produk.

        - Tambahkan tombol "Hapus" di setiap baris produk.

    ```
    <td>
        <!-- Tombol penambahan dan pengurangan amount -->
    </td>
    <td>
        <form method="POST" action="{% url 'main:delete_product' product.id %}">
            {% csrf_token %}
            <button type="submit" class="btn btn-danger btn-sm">Hapus</button>
        </form>
    </td>
    ```

    + **Membuat Fungsi View untuk Penghapusan Objek:**

        - Buka file `views.py` dan tambahkan fungsi view `delete_product` untuk menangani permintaan pengguna ketika mereka mengklik tombol "Hapus".

    ```
    @login_required(login_url='/login')
    def delete_product(request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        if request.method == 'POST':
            product.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
    ```

    + **Tambahkan URL untuk Fungsi View Baru:**

        - Buka file `urls.py` dalam aplikasi Anda dan tambahkan URL untuk view `delete_product`.

    ```
    urlpatterns = [
        # URL lainnya
        path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    ]
    ```

    + **Terapkan Perubahan di Template**: 
    
    Pastikan perubahan HTML di template sudah sesuai dengan langkah-langkah di atas.

    + **Uji Coba**: 
    
    Jalankan server Django Anda (`python manage.py runserver`) dan uji coba fitur penghapusan objek.


# Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS

## Jawaban Pertanyaan

__1.  Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.__

_Jawab:_ 

Element selector (selektor elemen) adalah salah satu jenis selektor dalam CSS yang digunakan untuk memilih dan menggaya elemen HTML berdasarkan nama elemennya. Manfaat element selector adalah sebagai berikut:

    
    + Seleksi Elemen Tertentu: Element selector memungkinkan kita untuk memilih elemen HTML tertentu berdasarkan tag-nya, misalnya <p> untuk paragraf, <h1> untuk judul level 1, dll.

    + Gaya Umum: Element selector sering digunakan untuk menerapkan gaya yang sama pada elemen-elemen dengan tag yang sama dalam halaman web.

    +Sederhana: Penggunaan element selector adalah yang paling sederhana dalam CSS.

*Jenis-Jenis Selektor Elemen CSS:*

    - **Selektor Elemen Tunggal**: Ini adalah jenis selektor elemen yang paling sederhana, yang memilih elemen berdasarkan tag-nya. Contoh:

    ```css
    p {
        /* Gaya untuk semua elemen <p> dalam dokumen */
    }
    ```

    - **Selektor Elemen Bersarang**: Selektor ini digunakan untuk memilih elemen yang berada dalam elemen lain. Contoh:

    ```css
    ul li {
        /* Gaya untuk semua elemen <li> yang berada dalam elemen <ul> */
    }
    ```

    - **Selektor Kelas**: Selektor ini memungkinkan kita untuk memilih elemen berdasarkan nilai atribut `class` yang diberikan pada elemen. Contoh:

    ```css
    .btn {
        /* Gaya untuk semua elemen yang memiliki kelas "btn" */
    }
    ```

    - **Selektor ID**: Selektor ini digunakan untuk memilih elemen berdasarkan nilai atribut `id` yang diberikan pada elemen. ID harus unik dalam satu halaman. Contoh:

    ```css
    #header {
        /* Gaya untuk elemen dengan id "header" */
    }
    ```

    - **Selektor Elemen Grup**: Ini memungkinkan kita untuk menerapkan gaya pada beberapa elemen dengan jenis elemen yang berbeda dalam satu aturan CSS. Contoh:
    ```css

    h1, h2, h3 {
        /* Gaya untuk elemen <h1>, <h2>, dan <h3> */
    }
    ```

    - **Selektor Universal**: Selektor ini memilih semua elemen dalam dokumen. Contoh:

    ```css
    * {
        /* Gaya untuk semua elemen dalam dokumen */
    }
    ```

    - **Pseudo-class Selector**: Ini adalah selektor yang digunakan untuk memilih elemen berdasarkan kondisi atau keadaan elemen, seperti `:hover`, `:active`, dan lainnya. Contoh:

    ```css
    a:hover {
        /* Gaya untuk tautan saat mouse di atasnya */
    }
    ```


__1.  Jelaskan HTML5 Tag yang kamu ketahui.__

_Jawab:_ 

1. `<header>`: Digunakan untuk menunjukkan bagian atas atau kepala dari sebuah halaman atau elemen. Biasanya berisi elemen-elemen seperti judul, logo, atau tautan menu utama.

2. `<nav>`: Digunakan untuk mengelompokkan tautan menu navigasi. Ini membantu dalam membedakan bagian yang berisi tautan navigasi dari konten lainnya.

3. `<section>`: Mengelompokkan konten yang terkait secara tematik dalam sebuah halaman. Ini membantu dalam mengorganisasi konten yang terkait dalam satu unit.

4. `<article>`: Menandakan konten yang independen dan memiliki makna secara mandiri. Ini digunakan untuk artikel, berita, atau postingan blog yang dapat berdiri sendiri.

5. `<footer>`: Merupakan bagian bawah dari sebuah elemen atau halaman web, biasanya berisi informasi seperti hak cipta, informasi kontak, atau tautan ke halaman terkait.

6. `<aside>`: Digunakan untuk konten yang terkait dengan konten di sekitarnya dan dapat dianggap sebagai "sampingan." Biasanya digunakan untuk informasi tambahan, tautan terkait, atau iklan sampingan.

7. `<figure>`: Digunakan untuk mengelompokkan konten media, seperti gambar, audio, atau video, beserta elemen `<figcaption>` untuk memberikan deskripsi singkat.

8. `<table>`: Tag ini digunakan untuk membuat tabel dalam dokumen HTML. Tabel dapat berisi baris dan kolom yang membentuk grid untuk menampilkan data tabular.

9. `<tr>` (Table Row): Tag ini digunakan untuk mendefinisikan baris dalam tabel. Setiap `<tr>` berisi satu atau lebih elemen `<td>` atau `<th>` yang membentuk sel-sel dalam baris tersebut.

10. `<th>` (Table Header Cell): Tag ini digunakan untuk mendefinisikan sel kepala (header) dalam tabel.

11. `<td>` (Table Data Cell): Tag ini digunakan untuk mendefinisikan sel data dalam tabel. Sel-sel data berisi informasi atau data yang ingin ditampilkan dalam tabel.


__1.  Jelaskan perbedaan antara margin dan padding.__

_Jawab:_ 

Perbedaan antara margin dan padding adalah sebagai berikut:

    1. **Margin**: Margin adalah ruang kosong di sekitar elemen HTML. Ini adalah jarak antara elemen dengan elemen-elemen lain di sekitarnya. Margin tidak memiliki warna latar belakang dan tidak memiliki pengaruh visual pada elemen itu sendiri. Margin berguna untuk mengatur jarak antara elemen-elemen dalam layout.

    1. **Padding**: Padding adalah ruang kosong di antara konten elemen dan batas elemen itu sendiri. Ini adalah jarak antara konten elemen dan batas elemen. Padding dapat memiliki warna latar belakang dan akan mempengaruhi tampilan visual elemen itu sendiri.

Maka ditarik kesimpulan, properti margin mengontrol ruang di luar elemen, dan properti padding mengontrol ruang di dalam elemen. Margin digunakan untuk menyesuaikan jarak elemen terhadap elemen lain (misalnya div terhadap div lain di halaman), dan padding digunakan untuk menyesuaikan tampilan elemen individu (misalnya jumlah piksel antara tepi div dan teks di dalamnya).


__1.  Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?__

_Jawab:_ 

**Tailwind CSS**:

1. **Pendekatan Modular**: Tailwind CSS menggunakan pendekatan yang sangat modular dengan memanfaatkan utilitas CSS yang telah diatur sebelumnya. Ini memungkinkan pengembang untuk membangun elemen UI dengan menumpuk kelas-kelas utilitas.

2. **Fleksibilitas Tinggi**: Tailwind memberikan kontrol yang tinggi atas desain dan tampilan elemen UI. Anda dapat dengan mudah menyesuaikan setiap aspek tampilan sesuai kebutuhan.

3. **Ukuran File Kecil**: Karena Anda hanya memuat utilitas CSS yang diperlukan, ukuran file akhir cenderung lebih kecil, menghasilkan waktu pemuatan yang lebih cepat.

4. **Penggunaan Utilitas**: Tailwind menggunakan utilitas CSS seperti `mx-4`, `bg-blue-500`, dan `text-center` untuk mengatur margin, latar belakang, dan tata letak elemen.


**Bootstrap**:

1. **Kumpulan Komponen Siap Pakai**: Bootstrap menyediakan kumpulan besar komponen UI yang telah di-styling sebelumnya, seperti tombol, jumbotron, dan formulir. Ini memungkinkan pembuatan halaman web dengan cepat.

2. **Kebutuhan Desain yang Konsisten**: Bootstrap dirancang untuk memastikan kekonsistenan desain dalam proyek. Ini cocok untuk proyek yang menginginkan tampilan yang seragam di seluruh halaman web.

3. **Ukuran File Lebih Besar**: Karena Bootstrap menyertakan banyak komponen dan fitur, ukuran file Bootstrap cenderung lebih besar, yang dapat mempengaruhi waktu pemuatan halaman.

4. **Penggunaan Kelas-Kelas CSS**: Bootstrap menggunakan kelas-kelas CSS seperti `btn`, `bg-primary`, dan `text-center` untuk mengatur tampilan elemen.


**Kesimpulan**:

- **Tailwind CSS** menekankan fleksibilitas tinggi, modularitas, dan penggunaan utilitas CSS.

- **Bootstrap** lebih berfokus pada kemudahan penggunaan, kumpulan komponen siap pakai, dan konsistensi desain.
- Pilihan antara keduanya tergantung pada kebutuhan dan preferensi proyek web Anda.


__1.  Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).__

_Jawab:_ 

Untuk menyelesaikan checklist, saya melakukan beberapa perubahan pada code saya.

1. **edit**
    
    Disini menambahkan beberapa potongan kode pada `views.py`. 

    ```
    @login_required(login_url='/login')
    def edit_product(request, id):
    # Get product berdasarkan ID
    product = Product.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)
    ```

2. **merubah tampilan login**

    ```
    {% extends 'base.html' %}

    {% block meta %}
        <title>Login</title>
    {% endblock meta %}

    {% block content %}
    <style>
        /* Style untuk background halaman */
        body {
            background-color: #F5F5F5; /* Warna latar belakang halaman (cool tone) */
        }

        /* Style untuk konten login */
        .login-container {
            background-color: #FFFFFF; /* Warna background (putih) */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
            font-family: 'Helvetica Neue', sans-serif; /* Font elegan */
        }

        /* Style untuk tombol login dan register */
        .btn-login {
            background-color: #007BFF; /* Warna tombol (biru) */
            border: none;
            color: #fff; /* Warna teks tombol (putih) */
            font-weight: bold;
            transition: background-color 0.3s ease-in-out;
        }

        .btn-login:hover {
            background-color: #0056b3; /* Warna tombol saat hover (biru lebih gelap) */
        }

        .btn-register {
            background-color: #6C757D; /* Warna tombol register (abu-abu) */
            border: none;
            color: #fff; /* Warna teks tombol (putih) */
            font-weight: bold;
            transition: background-color 0.3s ease-in-out;
        }

        .btn-register:hover {
            background-color: #495057; /* Warna tombol saat hover (abu-abu lebih gelap) */
        }
    </style>

    <div class="container mt-5">
        <div class="row">
            <div class="col-lg-6 offset-lg-3">
                <div class="card login-container">
                    <div class="card-body">
                        <h2 class="card-title text-center mb-4">Welcome to RushyRushy</h2>
                        <hr>

                        <div id="loginCarousel" class="carousel slide mb-4" data-ride="carousel">
                            <!-- Isi Carousel Sesuai Keinginanmu -->
                            <div class="carousel-inner">
                                <!-- Slide 1 -->
                                <div class="carousel-item active">
                                    <h4 class="text-center">Who Are You?</h4>
                                    <div class="text-center">
                                        <button class="btn btn-primary btn-lg mr-3" data-toggle="modal" data-target="#loginModal">Login</button>
                                        <a href="{% url 'main:register' %}" class="btn btn-secondary btn-lg">Register</a>
                                    </div>
                                </div>

                                <!-- Slide 2 -->
                                <div class="carousel-item">
                                    <h4 class="text-center">Fun Fact About Antique Stuff</h4>
                                    <p class="text-center">Did you know that antique items can hold hidden stories of the past?</p>
                                </div>

                                <!-- Slide 3 -->
                                <div class="carousel-item">
                                    <h4 class="text-center">Discover Our App</h4>
                                    <p class="text-center">Explore our amazing app features and start your journey today!</p>
                                </div>
                            </div>

                            <!-- Carousel Controls -->
                            <a class="carousel-control-prev" href="#loginCarousel" role="button" data-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="sr-only">Previous</span>
                            </a>
                            <a class="carousel-control-next" href="#loginCarousel" role="button" data-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="sr-only">Next</span>
                            </a>
                        </div>

                        <div class="text-center">
                            <p id="registrationAlert" class="d-none alert alert-danger">Don't have an account yet? <a href="{% url 'main:register' %}" class="btn-link btn-register">Register Now</a></p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- Login Modal -->
    <div class="modal fade" id="loginModal" tabindex="-1" role="dialog" aria-labelledby="loginModalLabel" aria-hidden="true">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title" id="loginModalLabel">Login</h5>
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                        <span aria-hidden="true">&times;</span>
                    </button>
                </div>
                <div class="modal-body">
                    <form method="POST" action="{% url 'main:login' %}">
                        {% csrf_token %}
                        <div class="form-group">
                            <label for="username">Username:</label>
                            <input type="text" name="username" id="username" class="form-control" required>
                        </div>
                        <div class="form-group">
                            <label for="password">Password:</label>
                            <input type="password" name="password" id="password" class="form-control" required>
                        </div>
                        <div class="text-center">
                            <button type="submit" class="btn btn-primary btn-login">Login</button>
                        </div>
                    </form>
                </div>
            </div>
        </div>
    </div>

    {% endblock content %}

    ```

3. **merubah tampilan register**

    ```
    {% extends 'base.html' %}

    {% block meta %}
        <title>Register</title>
    {% endblock meta %}

    {% block content %}
    <style>
        /* Style untuk konten register */
        .register-container {
            background-color: #F5F5F5; /* Warna background halaman (cool tone) */
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
            font-family: 'Helvetica Neue', sans-serif; /* Font yang lebih formal */
        }

        /* Style untuk tombol daftar dan tombol kembali */
        .btn-register {
            background-color: #007BFF; /* Warna background tombol daftar (biru) */
            border: none;
            color: #fff; /* Warna teks tombol (putih) */
            font-weight: bold;
            transition: background-color 0.3s ease-in-out;
        }

        .btn-register:hover {
            background-color: #0056b3; /* Warna tombol saat hover (biru lebih gelap) */
        }

        .btn-back {
            background-color: #6C757D; /* Warna background tombol kembali (abu-abu) */
            border: none;
            color: #fff; /* Warna teks tombol (putih) */
            font-weight: bold;
            transition: background-color 0.3s ease-in-out;
        }

        .btn-back:hover {
            background-color: #495057; /* Warna tombol saat hover (abu-abu lebih gelap) */
        }
    </style>

    <div class="container mt-5">
        <div class="row">
            <div class="col-lg-6 offset-lg-3">
                <div class="card register-container">
                    <div class="card-body">
                        <h2 class="card-title text-center mb-4">Register</h2>

                        <form method="POST">
                            {% csrf_token %}
                            {{ form.as_p }} <!-- Menggunakan as_p untuk menampilkan form sebagai paragraf -->
                            <div class="text-center">
                                <a href="{% url 'main:login' %}" class="btn btn-secondary btn-back">Back</a>
                                <button type="submit" class="btn btn-primary btn-register">Register</button>
                            </div>
                        </form>

                        {% if messages %}
                            <ul>
                                {% for message in messages %}
                                    <li>{{ message }}</li>
                                {% endfor %}
                            </ul>
                        {% endif %}
                    </div>
                </div>
            </div>
        </div>
    </div>

    {% endblock content %}
    
    ```

4. **merubah tampilan tambah inventory**

    ```
    {% extends 'base.html' %}

    {% block meta %}
        <title>RushyRushy</title>
    {% endblock meta %}

    {% block content %}
    <style>
        /* Style untuk tampilan navbar */
        .navbar {
            background-color: #007BFF; /* Warna background navbar (biru) */
            color: #fff; /* Warna teks navbar (putih) */
        }

        /* Style untuk teks nama aplikasi di navbar */
        .navbar-brand {
            color: #fff !important; /* Warna teks nama aplikasi (putih) */
            font-size: 24px; /* Ukuran font nama aplikasi */
        }

        /* Style untuk bilah pencarian di navbar */
        .navbar-search {
            width: 300px; /* Lebar bilah pencarian */
            text-align: center; /* Pusatkan isi bilah pencarian */
        }

        /* Style untuk card produk */
        .product-card {
            margin-bottom: 20px;
            background-color: #FFFFFF; /* Warna background card produk (putih) */
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.3);
            transition: transform 0.3s ease-in-out;
        }

        /* Hover effect untuk card produk */
        .product-card:hover {
            transform: scale(1.05); /* Membesarkan card saat hover */
            box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.3); /* Bayangan lebih besar saat hover */
        }

        /* Style untuk card header */
        .card-header {
            background-color: #007BFF; /* Warna background card header (biru) */
            color: #fff; /* Warna teks card header (putih) */
        }

        /* Style untuk tombol "Tampilkan Detail" di Collapse */
        .btn-collapse {
            background-color: #007BFF; /* Warna background tombol (biru) */
            border: none;
            color: #fff; /* Warna teks tombol (putih) */
            font-weight: bold;
        }

        .btn-collapse:hover {
            background-color: #0056b3; /* Warna tombol saat hover (biru lebih gelap) */
        }

        /* Style untuk informasi pengguna */
        .user-info {
            background-color: #F5F5F5; /* Warna background informasi pengguna (cool tone) */
            padding: 15px;
            border-radius: 10px;
            margin-top: 20px;
        }

        /* Style untuk judul informasi pengguna */
        .user-info-title {
            font-size: 18px;
            font-weight: bold;
        }

        /* Style untuk tombol logout */
        .logout-btn {
            background-color: #6C757D; /* Warna background tombol logout (abu-abu) */
            color: #fff; /* Warna teks tombol logout (putih) */
        }

        .logout-btn:hover {
            background-color: #495057; /* Warna tombol saat hover (abu-abu lebih gelap) */
        }
    </style>

    <nav class="navbar navbar-expand-lg navbar-light">
        <div class="container">
            <a class="navbar-brand" href="#">RushyRushy</a>

            <!-- Bilah pencarian di tengah navbar -->
            <form class="form-inline navbar-search">
                <input class="form-control mr-sm-2" type="search" placeholder="Search for items..." aria-label="Search">
                <button class="btn btn-outline-light my-2 my-sm-0" type="submit">Search</button>
            </form>

            <!-- Tombol keluar yang mengarah ke halaman Login -->
            <a href="{% url 'main:login' %}" class="btn btn-danger ml-auto logout-btn">Logout</a>
        </div>
    </nav>

    <div class="container mt-4">
        <!-- Tambahkan Bootstrap Collapse untuk informasi pengguna -->
        <button class="btn btn-collapse" type="button" data-toggle="collapse" data-target="#collapseDetails" aria-expanded="false" aria-controls="collapseDetails">
            Show User Details
        </button>

        <div class="collapse mt-3" id="collapseDetails">
            <!-- Card Bootstrap untuk informasi pengguna -->
            <div class="card user-info">
                <div class="card-header">
                    <h5 class="card-title user-info-title">User Information</h5>
                </div>
                <div class="card-body">
                    <p><strong>Username:</strong> {{ name }}</p>
                    <p><strong>Class:</strong> {{ class }}</p>
                    <p><strong>Total items saved:</strong> {{ total_items }}</p>
                </div>
            </div>
        </div>

        <!-- Loop melalui produk dan menampilkan card untuk setiap produk -->
        <div class="row">
            {% for product in products %}
            <div class="col-lg-4">
                <div class="card product-card">
                    <div class="card-body">
                        <h5 class="card-title">{{ product.name }}</h5>
                        <p class="card-text">{{ product.description }}</p>
                        <p class="card-text"><strong>Price:</strong> {{ product.price }}</p>
                    </div>
                    <div class="card-footer">
                        <button type="button" class="btn btn-primary" data-toggle="modal" data-target="#productDetails{{ product.id }}">
                            Details
                        </button>
                    </div>
                </div>
            </div>
            <!-- Modal untuk menampilkan detail produk -->
            <div class="modal fade" id="productDetails{{ product.id }}" tabindex="-1" role="dialog" aria-labelledby="productDetailsLabel{{ product.id }}" aria-hidden="true">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title" id="productDetailsLabel{{ product.id }}">Product Details: {{ product.name }}</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                                <span aria-hidden="true">&times;</span>
                            </button>
                        </div>
                        <div class="modal-body">
                            <p><strong>Product Name:</strong> {{ product.name }}</p>
                            <p><strong>Price:</strong> {{ product.price }}</p>
                            <p><strong>Date Added:</strong> {{ product.date_added }}</p>
                            <p><strong>Description:</strong> {{ product.description }}</p>
                            <!-- Menambahkan tulisan "Quantity:" -->
                            <p><strong>Quantity:</strong>
                                <div class="d-flex justify-content-between align-items-center">
                                    <div>
                                        <!-- Tombol Kurang -->
                                        <form method="POST" action="{% url 'main:decrement_stock' product.id %}">
                                            {% csrf_token %}
                                            <button type="submit" class="btn btn-sm btn-danger ml-2">-</button>
                                        </form>
                                    </div>
                                    <!-- Menampilkan jumlah -->
                                    <span id="amount{{ product.id }}">{{ product.amount }}</span>
                                    <div>
                                        <!-- Tombol Tambah -->
                                        <form method="POST" action="{% url 'main:increment_stock' product.id %}">
                                            {% csrf_token %}
                                            <button type="submit" class="btn btn-sm btn-success mr-2">+</button>
                                        </form>
                                    </div>
                                </div>
                            </p>
                            <p><strong>Category:</strong> {{ product.category }}</p>
                        </div>
                        <div class="modal-footer">
                            <!-- Tombol Edit -->
                            <a href="{% url 'main:edit_product' product.id %}" class="btn btn-primary">Edit</a>
                            <!-- Tombol Hapus -->
                            <form method="POST" action="{% url 'main:delete_product' product.id %}">
                                {% csrf_token %}
                                <button type="submit" class="btn btn-danger">Delete</button>
                            </form>
                        </div>
                    </div>
                </div>
            </div>

            {% endfor %}
        </div>

        <a href="{% url 'main:create_product' %}" class="btn btn-primary mt-4">Add New Product</a>

        <h5 class="mt-4">Last login session: {{ last_login }}</h5>
    </div>
{% endblock content %}
    ```

# Tugas 6: JavaScript dan Asynchronous JavaScript

## Jawaban Pertanyaan

__1. Jelaskan perbedaan antara asynchronous programming dengan synchronous programming.__

_Jawab:_

Perbedaan antara asynchronous programming dengan synchronous programming adalah bahwa asynchronous programming memungkinkan kode untuk berjalan secara bersamaan tanpa harus menunggu proses lain selesai, sedangkan synchronous programming membutuhkan kode untuk berjalan secara berurutan dan menunggu proses lain selesai sebelum melanjutkan. Contoh asynchronous programming adalah menggunakan fungsi callback, promise, atau async/await di JavaScript, yang dapat menangani operasi yang membutuhkan waktu lama seperti permintaan jaringan atau akses database tanpa menghalangi jalannya program. Contoh synchronous programming adalah menggunakan loop for, while, atau if-else di JavaScript, yang harus mengevaluasi kondisi atau mengulangi perintah secara berurutan.


__2. Dalam penerapan JavaScript dan AJAX, terdapat penerapan paradigma event-driven programming. Jelaskan maksud dari paradigma tersebut dan sebutkan salah satu contoh penerapannya pada tugas ini.__

_Jawab:_

Paradigma event-driven programming adalah paradigma pemrograman yang mengatur alur program berdasarkan kejadian (event) yang terjadi di dalam program6. Kejadian tersebut bisa berasal dari interaksi pengguna, output sensor, atau pesan dari program atau thread lain. Contoh penerapan paradigma event-driven programming pada JavaScript dan AJAX adalah menggunakan event listener, yang memungkinkan fungsi tertentu untuk dipanggil ketika event tertentu terjadi. Misalnya, kita bisa menggunakan event listener untuk menangani event klik pada sebuah tombol, yang akan memicu fungsi untuk mengirim permintaan AJAX ke server dan menerima tanggapan.

__3. Jelaskan penerapan asynchronous programming pada AJAX.__

_Jawab:_

Penerapan asynchronous programming pada AJAX adalah menggunakan teknik yang memungkinkan JavaScript untuk mengirim permintaan ke server tanpa harus menunggu tanggapan, dan melanjutkan eksekusi kode lainnya yang membuat halaman web tetap responsif. Asynchronous programming pada AJAX dapat dilakukan dengan menggunakan beberapa metode, seperti XMLHttpRequest (XHR), jQuery.ajax(), atau Fetch API. Metode-metode ini memungkinkan kita untuk menentukan fungsi callback yang akan dipanggil ketika tanggapan dari server diterima, dan melakukan operasi sesuai dengan data yang diterima.

__4. Pada PBP kali ini, penerapan AJAX dilakukan dengan menggunakan Fetch API daripada library jQuery. Bandingkanlah kedua teknologi tersebut dan tuliskan pendapat kamu teknologi manakah yang lebih baik untuk digunakan.__

_Jawab:_

Fetch API dan jQuery.ajax() adalah dua teknologi yang dapat digunakan untuk melakukan permintaan AJAX dengan JavaScript. Keduanya memiliki kelebihan dan kekurangan masing-masing. Beberapa perbedaan antara Fetch API dan jQuery.ajax() adalah sebagai berikut:

| Fetch API  | 	jQuery.ajax() |
| ------------- | ------------- |
| Merupakan teknologi baru yang didukung oleh browser modern  | Merupakan library JavaScript yang sudah lama digunakan dan didukung oleh banyak browser  |
| Menggunakan promise untuk menangani hasil permintaan  | Menggunakan callback atau promise untuk menangani hasil permintaan  |
| Tidak menolak promise ketika status HTTP error, tetapi hanya ketika ada kesalahan jaringan atau permintaan gagal  | Menolak promise ketika status HTTP error atau ada kesalahan jaringan  |
| Secara default tidak mengirim atau menerima cookie dari server, kecuali jika ditentukan opsi credentials  | Secara default mengirim dan menerima cookie dari server  |
| Memiliki metode bawaan untuk mengubah data menjadi berbagai format, seperti text, json, blob, dll.  | Tergantung pada format data yang dikirim oleh server  |

Menurut pendapat saya, teknologi yang lebih baik untuk digunakan tergantung pada kebutuhan dan preferensi masing-masing pengembang. Fetch API memiliki keuntungan dalam hal kemudahan penggunaan, kemodernan, dan fleksibilitas. Namun, jQuery.ajax() memiliki keuntungan dalam hal kompatibilitas browser, penanganan error, dan konsistensi format data. 

__5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).__

_Jawab:_

