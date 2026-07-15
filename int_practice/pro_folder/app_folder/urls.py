from django.urls import path
from . import views

app_name = 'app_folder'
urlpatterns = [
    # path('home/', views.home, name='home'),
    # path('list/', views.productlist, name='product_list'),
    # path('create/', views.createproduct, name='create_product'),
    # path('update/<int:id>/', views.updateproduct, name='updateproduct'),
    # path('delete/<int:id>/', views.deleteproduct, name='deleteproduct'),

    path('api/', views.ProductAPI.as_view()),
    path('api/<int:id>/', views.ProductAPI.as_view()),
]
