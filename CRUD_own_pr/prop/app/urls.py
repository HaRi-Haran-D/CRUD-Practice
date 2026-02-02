from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('list/',views.list, name='list'),
    path('update/<int:item_id>/', views.update, name='update'),
    path('delete/<int:item_id>/', views.delete, name='delete')
]
