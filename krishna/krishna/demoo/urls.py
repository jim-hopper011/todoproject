from . import views
from django.urls import path

urlpatterns = [
    path('', views.d1, name='demo'),
    # path('add/', views.add, name='add')
]