from django.urls import path
from . import views

urlpatterns = [
    path('products/create/', views.create_product, name='create_product'),
    path('products/<int:pk>/update/', views.update_product, name='update_product'),
    path('products/<int:pk>/delete/', views.delete_product, name='delete_product'),
    path('orders/create/', views.create_order, name='create_order'),
    path('orders/<int:pk>/update/', views.update_order, name='update_order'),
    path('orders/<int:pk>/delete/', views.delete_order, name='delete_order'),
]