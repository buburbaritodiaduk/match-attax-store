from django.shortcuts import render, redirect, get_object_or_404, reverse
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags


@login_required(login_url='/login')
def show_main(request):
    product_list = Product.objects.all()
    filter_type = request.GET.get("filter", "all")
    if filter_type == "all":
        product_list = Product.objects.all()
    else:
        product_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406438214',
        'name': 'Aryandana Pascua Patiung',
        'class': 'PBP F',
        'product_list': product_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),

    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        news_entry = form.save(commit = False)
        news_entry.user = request.user
        news_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "product_news.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, id=id)

    context = {
        'product': product
    }

    return render(request, "product_detail.html", context)

def show_xml(request):
    product_list = Product.objects.all()
    xml_data = serializers.serialize("xml", product_list)
    return HttpResponse(xml_data, content_type="application/xml")

# Jangan lupa import di bagian atas file views.py
from django.http import JsonResponse
from .models import Product # Sesuaikan dengan lokasi models.py kamu

def show_json(request):
    # Mengambil semua objek dari model Product
    product_list = Product.objects.all()
    
    # Mengubah queryset menjadi list of dictionaries
    data = [
        {
            'id': str(product.id),         
            'name': product.name,           
            'price': product.price,        
            'description': product.description, 
            'thumbnail': product.thumbnail,
            'category': product.category,
            'is_featured': product.is_featured,
            'created_at': product.created_at.isoformat(), 
            'user_id': product.user_id,  
        }
        for product in product_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
    try:
        product_item = Product.objects.filter(pk=product_id)
        xml_data = serializers.serialize("xml", product_item)
        return HttpResponse(xml_data, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(Status=404)


def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        
        data = {
            'id': str(product.id),
            'name': product.name,           
            'price': product.price,         
            'description': product.description, 
            'category': product.category,
            'thumbnail': product.thumbnail,
            'is_featured': product.is_featured,
            'created_at': product.created_at.isoformat(),
            'user_id': product.user_id,
            'user_username': product.user.username if product.user else None,
        }
        return JsonResponse(data)

    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Product not found'}, status=404)

# main/views.py
import json # Pastikan ini ada di atas
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

@csrf_exempt
def register_ajax(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Account created successfully!'}, status=201)
        else:
            # Kirim error form sebagai JSON
            return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    # Me-render halaman jika diakses via GET
    return render(request, 'register.html', {'form': UserCreationForm()})

@csrf_exempt
def login_ajax(request):
    if request.method == 'POST':
        # Data dikirim sebagai JSON, jadi kita perlu load dari request.body
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            response = JsonResponse({'status': 'success', 'message': 'Login successful!'})
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            return JsonResponse({'status': 'error', 'message': 'Invalid username or password'}, status=401)
    # Me-render halaman jika diakses via GET
    return render(request, 'login.html', {'form': AuthenticationForm()})

@csrf_exempt
def logout_ajax(request):
    if request.method == "POST":
        logout(request)
        return JsonResponse({"status": "success", "message": "Logout successful!"})
    else:
        # kalau bukan POST (misalnya user klik langsung link), redirect aja biar aman
        logout(request)
        return redirect('main:login')

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form,
        'product': product
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = Product.objects.get(pk = id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_POST
def add_product_ajax(request):
    # Pastikan kamu mengambil "name", BUKAN "title"
    name = strip_tags(request.POST.get("name"))
    price = request.POST.get("price")
    description = strip_tags(request.POST.get("description"))
    category = request.POST.get("category")
    thumbnail = strip_tags(request.POST.get("thumbnail"))
    is_featured = request.POST.get("is_featured") == 'on'
    user = request.user

    # Buat objek Product baru dengan variabel yang benar
    new_product = Product(
        name=name,
        price=price,
        description=description,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_product.save()

    # Siapkan data JSON untuk dikirim kembali
    data = {
        'id': str(new_product.id),
        'name': new_product.name,
        'price': new_product.price,
        'description': new_product.description,
        'category': new_product.category,
        'thumbnail': new_product.thumbnail,
        'is_featured': new_product.is_featured,
        'created_at': new_product.created_at.isoformat(),
        'user_id': new_product.user.id,
    }
    
    return JsonResponse(data, status=201)

@csrf_exempt
@require_POST
def update_product_ajax(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        
        # Ambil data baru dari form dan bersihkan
        product.name = strip_tags(request.POST.get("name"))
        product.price = request.POST.get("price")
        product.description = strip_tags(request.POST.get("description"))
        product.category = request.POST.get("category")
        product.thumbnail = strip_tags(request.POST.get("thumbnail"))
        product.is_featured = request.POST.get("is_featured") == 'on'
        
        # Simpan perubahan ke database
        product.save()
        
        return JsonResponse({'status': 'success', 'message': 'Product updated successfully'}, status=200)

    except Product.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product not found'}, status=404)
    
@csrf_exempt
@require_POST # Menggunakan POST untuk keamanan, agar tidak bisa dihapus via URL biasa
def delete_product_ajax(request, product_id):
    try:
        product = Product.objects.get(pk=product_id)
        # Pastikan hanya user yang membuat produk yang bisa menghapusnya
        if product.user == request.user:
            product.delete()
            return JsonResponse({'status': 'success', 'message': 'Product deleted successfully'}, status=200)
        else:
            return JsonResponse({'status': 'error', 'message': 'Unauthorized'}, status=403)
    except Product.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product not found'}, status=404)