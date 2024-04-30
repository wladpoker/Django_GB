from django.contrib import admin

from django.urls import path
from shopapp import views

urlpatterns = [
    path('', views.home, name='home'),  # URL для представления "главная"
    path('orders/', views.orders, name='orders'),  # URL для представления "главная"
    path('about/', views.about, name='about'),  # URL для представления "о себе"
]
