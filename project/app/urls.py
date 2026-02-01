from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('list/', views.list_items, name='list_items'),
    path('update/<int:item_id>/', views.update_list, name='update_list'),
    path('delete/<int:item_id>/', views.delete_list, name='delete_list'),
]