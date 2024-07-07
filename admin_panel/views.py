# admin_panel/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from store.models import Category, Product, ProductImage
from .forms import ProductForm, ProductImageForm
from .forms import CategoryForm
from PIL import Image
import os

User = get_user_model()

def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('admin_panel:dashboard')
        else:
            messages.error(request, 'Invalid credentials or not an admin')
    return render(request, 'admin_panel/admin_login.html')

@login_required
def admin_dashboard(request):
    return render(request, 'admin_panel/admin_dashboard.html')





def admin_logout(request):
    logout(request)
    return redirect('admin_panel:login')

def manage_users(request):
    users = User.objects.all()
    return render(request, 'admin_panel/manage_users.html', {'users': users})

def toggle_user_status(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = not user.is_active
    user.save()
    return redirect('admin_panel:manage_users')


def manage_categories(request):
    categories = Category.objects.filter(is_deleted=False)
    return render(request, 'admin_panel/manage_categories.html', {'categories': categories})
@login_required
def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:manage_categories')
    else:
        form = CategoryForm()
        #name = request.POST['name']
        #Category.objects.create(name=name)
        #return redirect('admin_panel:manage_categories')
    return render(request, 'admin_panel/add_category.html',{'form':form})


def edit_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return redirect('admin_panel:manage_categories')  # Correct URL name
    else:
        form = CategoryForm(instance=category)
    return render(request, 'admin_panel/edit_category.html', {'form': form, 'category': category})

def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.is_deleted = True
    category.save()
    return redirect('admin_panel:manage_categories')



def manage_products(request):
    products = Product.objects.filter(is_deleted=False)
    return render(request, 'admin_panel/manage_products.html', {'products': products})

'''def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            images = request.FILES.getlist('images')
            for img in images:
                image = Image.open(img)
                image = image.resize((500, 500))
                image_path = os.path.join('media/products', img.name)
                image.save(image_path)
                ProductImage.objects.create(product=product, image=image_path)
            return redirect('admin_panel:manage_products')
    else:
        form = ProductForm()
    return render(request, 'admin_panel/add_product.html', {'form': form})'''

def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            images = request.FILES.getlist('images')
            for img in images:
                ProductImage.objects.create(product=product, image=img)
            return redirect('admin_panel:manage_products')
    else:
        form = ProductForm()
    return render(request, 'admin_panel/add_product.html', {'form': form})
    
'''def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        files = request.FILES.getlist('images')
        if form.is_valid():
            form.save()
            for f in files:
                ProductImage.objects.create(product=product, image=f)
            return redirect('admin_panel:manage_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'admin_panel/edit_product.html', {'form': form, 'product': product})'''

def edit_product(request, product_id):
    product = Product.objects.get(id=product_id)
    categories = Category.objects.filter(is_deleted=False)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save()
            if 'images' in request.FILES:
                ProductImage.objects.filter(product=product).delete()
                images = request.FILES.getlist('images')
                for img in images:
                    ProductImage.objects.create(product=product, image=img)
            return redirect('admin_panel:manage_products')
    else:
        form = ProductForm(instance=product)
    return render(request, 'admin_panel/edit_product.html', {'form': form, 'product': product, 'categories': categories})


def delete_product(request, product_id):
    product = Product.objects.get(id=product_id)
    product.is_deleted = True
    product.save()
    return redirect('admin_panel:manage_products')
