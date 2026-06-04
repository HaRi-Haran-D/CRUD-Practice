from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    # path('register/', views.register, name='register'),
    # path('list/', views.list, name='list'),
    # path('login/',views.login, name='login'),
    # path('logout', views.logout, name='logout'),
    path('api/', views.StudentAPI.as_view(), name='api'),
    path('api/<int:id>/', views.StudentAPI.as_view(), name='api_id'),
]