"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('photo/', views.photo),
    path('xixi/', views.xixi),
    path('new_year/', views.new_year),
    path('photos/', views.photos),
    path('ElectronAlbum/', views.ElectronAlbum),
    path('FullPhoto/', views.FullPhoto),
    path('PhotoWall/', views.PhotoWall),
    path('WindowShades/', views.WindowShades),
    path('3dPhoto/', views.threePhoto),
    path('cube/', views.cube),
]
