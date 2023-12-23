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
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login  
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.views.decorators.http import require_http_methods
from .models import Product
import json



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

@csrf_exempt
def register_json(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)

    try:
        # Parse the JSON data
        data = json.loads(request.body)

        # Extract required data
        username = data['username']
        password = data['password']

        # Check if user already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({'error': 'Username already exists'}, status=400)

        # Create new user
        user = User.objects.create_user(username, password)
        user.save()

        return JsonResponse({'message': 'User registered successfully'}, status=201)

    except json.JSONDecodeError:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    except KeyError as e:
        return JsonResponse({'error': f'Missing key: {str(e)}'}, status=400)

    except Exception as e:
        # Log the exception for debugging
        print(f'Error in register_json: {e}')
        return JsonResponse({'error': 'Internal Server Error'}, status=500)


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
    
    # Jika produk yang akan dihapus adalah produk terakhir, maka cari produk sebelumnya
    if product.is_last:
        previous_product = Product.objects.filter(user=request.user, pk__lt=product_id).order_by('-pk').first()
        if previous_product:
            previous_product.is_last = True
            previous_product.save()

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
        amount = request.POST['amount']  # Ambil nilai amount dari form
        category = request.POST['category']

        # Dapatkan pengguna yang saat ini masuk
        current_user = request.user

        # Setel semua produk yang dimiliki pengguna ini menjadi bukan produk terakhir
        Product.objects.filter(user=request.user).update(is_last=False)

        # Simpan data produk ke dalam database dengan pengguna yang saat ini masuk
        product = Product(name=name, description=description, price=price, amount=amount, category=category, user=current_user, is_last=True)
        product.save()

        # Setelah produk berhasil ditambahkan, arahkan kembali ke halaman utama
        return redirect('main:show_main')
    else:
        # Jika metode bukan POST, tampilkan formulir kosong
        return render(request, 'create_product.html')

def get_product_json(request):
    product_item = Product.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))    

@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        amount = request.POST.get("amount")
        category = request.POST.get("category")
        date_added = request.POST.get("date_added")
        user = request.user

        new_product = Product(name=name, price=price, description=description, user=user)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()   

@csrf_exempt
def create_product_json(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Invalid request method'}, status=405)

    try:
        # Parse the JSON data
        product_data = json.loads(request.body)
        
        # Extract fields from the JSON data
        fields = product_data.get('fields', {})
        name = fields.get('name')
        date_added = fields.get('date_added')
        amount = fields.get('amount')
        description = fields.get('description')
        category = fields.get('category')
        price = fields.get('price')
        user_id = fields.get('user')
        is_last = fields.get('is_last', False)

       # Convert date_added to datetime object
        date_added = datetime.datetime.strptime(date_added, '%Y-%m-%d').date()

        # Get user model
        user = get_user_model().objects.get(pk=user_id)

        # Create and save the new product
        new_product = Product(
            name=name,
            date_added=date_added,  # Use correct field name
            amount=amount,
            description=description,
            category=category,
            price=price,
            user=user,
            is_last=is_last  # Use correct field name
        )
        new_product.full_clean()  # Validate model instance
        new_product.save()

        return JsonResponse({'message': 'Product added successfully', 'product_id': new_product.pk}, status=201)

    except json.JSONDecodeError as e:
        return JsonResponse({'error': 'Invalid JSON data'}, status=400)

    except KeyError as e:
        return JsonResponse({'error': f'Missing key: {e}'}, status=400)

    except ValidationError as e:
        return JsonResponse({'error': f'Validation error: {e}'}, status=400)

    except get_user_model().DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

    except Exception as e:
        # Log the exception for debugging
        print(f'Error in create_product_json: {e}')
        return JsonResponse({'error': 'Internal Server Error'}, status=500)


# Mengedit produk
@require_http_methods(["POST"])
def edit_product_json(request, id):
    try:
        product = Product.objects.get(pk=id)
        data = json.loads(request.body)
        product.name = data.get('name', product.name)
        product.price = data.get('price', product.price)
        product.description = data.get('description', product.description)
        # Update field lain jika ada
        product.save()
        return JsonResponse({'message': 'Produk berhasil diperbarui'})
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Produk tidak ditemukan'}, status=404)
    except KeyError:
        return JsonResponse({'error': 'Data tidak lengkap'}, status=400)


# Menghapus produk
@require_http_methods(["DELETE"])
def delete_product_json(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        product.delete()
        return JsonResponse({'message': 'Produk berhasil dihapus'}, status=200)
    except Product.DoesNotExist:
        return JsonResponse({'error': 'Produk tidak ditemukan'}, status=404)
