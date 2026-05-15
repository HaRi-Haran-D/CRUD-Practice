from django.urls import path
from . import views

app_name = 'app_folder'
urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.productlist, name='product_list'),
    path('create/', views.createproduct, name='create_product')
]