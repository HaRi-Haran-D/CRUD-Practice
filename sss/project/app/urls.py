
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.home, name='home'),
    path('', views.StudAPI.as_view(), name='student'),
    path('api/<int:id>/', views.StudAPIByID.as_view(), name='api_with_id'),
]
