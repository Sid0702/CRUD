"""
URL configuration for prj_restro project.

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
from django.urls import path
from app_restro.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('order-display/',order_display, name='order_display'),
    path('delete/<uuid:order_id>/', delete_order , name='delete_order'),
    path('edit/<uuid:order_id>/', edit_order, name='edit_order'),
    
    # path('delete/<int:pk>/', OrderDeleteView, name='delete_order')
]
