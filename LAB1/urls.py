"""
URL configuration for LAB1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from app.views import index, restaurant, restaurant_details, restaurant_add, restaurant_delete, restaurant_edit

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name="index"),
    path('restaurant/', restaurant, name="restaurants"),
    path('restaurant_details/<int:restaurant_id>/', restaurant_details, name='restaurant details'),
    path('restaurant_add/', restaurant_add, name='restaurant add'),
    path('restaurant_delete/<int:restaurant_id>/', restaurant_delete, name='restaurant delete'),
    path('restaurant_edit/<int:restaurant_id>/', restaurant_edit, name='restaurant edit'),
]