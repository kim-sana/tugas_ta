from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('', views.home, name='home'),  # Redirect ke halaman utama setelah login
    path('lihat/', views.lihat_data, name='lihat_data'),
    path('pencarian/', views.pencarian, name='pencarian'),
    path('tentang/', views.tentang, name='tentang'),  # URL untuk halaman tentang
]
