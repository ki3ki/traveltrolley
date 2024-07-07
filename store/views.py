'''from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def collections(request):
    return render(request, 'collections.html')
# Create your views here.'''
from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.
def home(request):
    return render(request, 'index.html')

def collections(request):
    categories = Category.objects.filter(is_deleted=False)
    return render(request, 'collections.html', {'categories': categories})

def category_detail(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug, is_deleted=False)
    products = Product.objects.filter(category=category, is_deleted=False)
    return render(request, 'category_detail.html', {'category': category, 'products': products})