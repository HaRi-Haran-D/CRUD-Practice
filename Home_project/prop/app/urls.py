from django.urls import path, include
from . import views

urlpatterns = [
    # path('home/',views.home, name='home'),
    # path('register/',views.register, name='register'),
    # path('', views.login, name="login"),
    # path('logout/', views.logout, name="logout"),
    path('api/', views.StudentView.as_view()),
    path('api/<int:id>/', views.StudentView.as_view()),
]