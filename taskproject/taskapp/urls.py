
from django.urls import path

from taskapp import views

urlpatterns = [
    path('', views.add, name='add'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('update/<int:id>/', views.update, name='update'),
    path('cbvhome/', views.TaskL.as_view(), name='cbvhome'),
    path('cbvdetail/<int:pk>/', views.TaskD.as_view(), name='cbvdetail'),
    path('cbvupdate/<int:pk>/', views.TaskU.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskR.as_view(), name='cbvdelete'),
]