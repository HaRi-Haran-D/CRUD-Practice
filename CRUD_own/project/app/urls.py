from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('list/', views.emp_list, name='list'),
    path('update/<int:item_id>/', views.update_list, name='update'),
    path('delete/<int:item_id>/', views.delete_list, name='delete'),
]