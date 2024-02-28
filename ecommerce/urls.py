"""
URL configuration for ecommerce project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from django.http import HttpResponse

def index(request):
    return HttpResponse('This is a custom url')

def new(request):
    return HttpResponse('This is next url')

urlpatterns = [
    path('adminss/', admin.site.urls),
    path('test/',index),
    path('test1/',new),
    path('products/',include('product.urls')),
    path('',include('userspage.urls')),
    path('admin/',include('adminpage.urls')),
]
