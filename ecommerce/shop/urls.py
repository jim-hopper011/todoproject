from shop import views
from django.urls import path
app_name = 'shop'

urlpatterns = [
    path('', views.all, name='all'),
    path('<slug:cslug>/', views.all, name='products_by_category'),
    path('<slug:cslug>/<slug:pslug>/', views.prodetail, name='prodetail'),
]

