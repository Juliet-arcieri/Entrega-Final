from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Página de inicio
    path('blogs/', views.blog_list, name='blog_list'),  # Lista de blogs
    path('blogs/<int:pk>/', views.blog_detail, name='blog_detail'),  # Detalle del blog
    path('about/', views.about, name='about'),  # Página "About"
    path('add/', views.add_blog, name='add_blog'),  # Añadir nuevo blog
]
