from django.urls import path
from . import views
app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.CreateEmployee.as_view(), name='create'),
    path('list/', views.ListEmployee.as_view(), name='list'),
    path('detail/<int:pk>/', views.EmployeeDetail.as_view(), name='detail'),
    path('update/<int:pk>/', views.UpdateEmployee.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteEmployee.as_view(), name='delete')
]