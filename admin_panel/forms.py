# admin_panel/forms.py
from django import forms
from store.models import Product, ProductImage, Category
from .custom_widgets import MultipleFileInput

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'image']


class ProductForm(forms.ModelForm):
    images = forms.ImageField(widget=MultipleFileInput, required=False)

    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'category']



class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ['image']