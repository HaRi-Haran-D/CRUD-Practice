from django.urls import path
from . import views
app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.CreateStudent.as_view(), name='create'),
    path('list/', views.StudentList.as_view(), name='list'),
    path('detail/<int:pk>/', views.StudentDetail.as_view(), name='detail'),
    path('update/<int:pk>/', views.UpdateStudent.as_view(), name='update'),
    path('delete/<int:pk>/', views.DeleteStudent.as_view(), name='delete'),
]