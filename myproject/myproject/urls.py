"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from miapp import views

urlpatterns = [
    path('', views.home, name='home'),  # Ruta para la página principal
    path('form/', views.form_view, name='form'),  # Ruta para el formulario
    path('pagina2/', views.pagina2, name='pagina2'),  # Ruta para pagina2.html
    path('pagina3/', views.pagina3, name='pagina3'),  # Ruta para pagina3.html
    path('pagina4/', views.pagina4, name='pagina4'),  # Ruta para pagina4.html
    path('pagina5/', views.pagina5, name='pagina5'),  # Ruta para pagina5.html
]