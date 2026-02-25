from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('list/', views.student_list, name='list'),
    path('update/<int:id>/', views.update_list, name='update'),
    path('delete/<int:id>/', views.delete_list, name='delete'),
]
