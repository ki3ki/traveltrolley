# admin_panel/urls.py
from django.urls import path
from .views import admin_login, admin_dashboard, manage_users, admin_logout, toggle_user_status
from .views import add_category, edit_category, delete_category , manage_categories
from .views import manage_products, add_product, edit_product, delete_product
#from . import views
app_name = 'admin_panel'

urlpatterns = [
    path('login/', admin_login, name='login'),
    path('dashboard/', admin_dashboard, name='dashboard'),
    path('manage_users/', manage_users, name='manage_users'),
    path('toggle_user_status/<int:user_id>/', toggle_user_status, name='toggle_user_status'),
    path('logout/', admin_logout, name='logout'),
    path('manage_categories/', manage_categories, name='manage_categories'),
    path('add_category/', add_category, name='add_category'),
    path('edit_category/<int:category_id>/', edit_category, name='edit_category'),
    path('delete_category/<int:category_id>/', delete_category, name='delete_category'),
    path('manage_products/', manage_products, name='manage_products'),
    path('add_product/', add_product, name='add_product'),
    path('edit_product/<int:product_id>/', edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', delete_product, name='delete_product'),
]

