"""
URL configuration for tools project.

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
import re
from django.conf.urls import handler404
from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'home'
handler404 = views.handler404
urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', include('Authentications.urls')),
    path('home/', views.home, name='home'),
    path('text_to_HTML/', include('text_to_HTML.urls')),
    path('TO_DO/', include('TO_DO.urls')),
    path('Weather/', include('Weather_App.urls')),
    path('Password_Storage/', include('Password_Storage.urls')),
    path('My_Contact/', include('My_Contact.urls')),
    path('admin/', admin.site.urls)
]
