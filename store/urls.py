from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/', views.collections, name='category'),  # updated from 'collections/' to 'category/'
    path('category/<slug:category_slug>/', views.category_detail, name='category_detail'),
]



