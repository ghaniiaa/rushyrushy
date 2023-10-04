import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponseRedirect
from main.forms import ProductForm
from django.urls import reverse
from .models import Product
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login  
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    total_items = products.count()  # Menghitung jumlah item yang tersimpan

    context = {
        'name': request.user.username,
        'class': 'PBP D',
        'products': products,
        'total_items': total_items,
        'last_login': request.COOKIES['last_login'],
    }
    return render(request, "main.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

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

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/login')
def increment_stock(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.amount += 1  # Menggunakan field amount untuk jumlah stok
        product.save()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def decrement_stock(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        if product.amount > 0:  # Menggunakan field amount untuk jumlah stok
            product.amount -= 1
            product.save()
    return HttpResponseRedirect(reverse('main:show_main'))

@login_required(login_url='/login')
def delete_product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

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

@login_required(login_url='/login')
def create_product(request):
    if request.method == 'POST':
        # Ambil data yang dikirimkan melalui form
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        category = request.POST['category']

        # Dapatkan pengguna yang saat ini masuk
        current_user = request.user

        # Simpan data produk ke dalam database dengan pengguna yang saat ini masuk
        product = Product(name=name, description=description, price=price, category=category, user=current_user)
        product.save()

        # Setelah produk berhasil ditambahkan, arahkan kembali ke halaman utama
        return redirect('main:show_main')

    # Jika request bukan POST, tampilkan halaman form kosong
    return render(request, 'create_product.html')