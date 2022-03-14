from django.urls import path
from . import views

app_name= 'cart'
urlpatterns = [
    path('add/<int:pid>/', views.add_cart, name='add_cart'),
    path('', views.cart_detail, name='cart_detail'),
    path('remove/<int:pid>/', views.item_remove, name='item_remove'),
    path('delete/<int:pid>/', views.delete, name='delete'),
]