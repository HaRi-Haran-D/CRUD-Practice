from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('list/', views.list_items, name='list_items'),
]