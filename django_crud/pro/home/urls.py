from django.urls import path
from . import views
app_name = 'home'

urlpatterns = [
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
    path('profile/<str:username>/', views.profile_view, name='profile'),
    path('userprofile/<str:username>/', views.userprofile, name='userprofile'),
]