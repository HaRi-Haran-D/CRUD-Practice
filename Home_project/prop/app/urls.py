from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import *
from .serializers import *
from . import views


router = DefaultRouter()
router.register(r'route', views.DataBaseView)


urlpatterns = [
    # path('home/',views.home, name='home'),
    # path('register/',views.register, name='register'),
    # path('', views.login, name="login"),
    # path('logout/', views.logout, name="logout"),

    path('', include(router.urls)),
    path('api/', views.StudentView.as_view()),
    path('api/<int:id>/', views.StudentView.as_view()),
    path('users/', views.UserView.as_view(queryset=User.objects.all(), serializer_class=UserSerializer), name='user-list')
]