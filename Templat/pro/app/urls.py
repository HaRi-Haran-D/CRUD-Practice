from django.urls import path
from . import views

app_name = 'app'
urlpatterns = [
    path('', views.home, name='home'),
    path('<int:id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete')
]
