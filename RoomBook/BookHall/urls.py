from django.urls import path
from .views import *


urlpatterns = [
    path('', RoomBookView.as_view()),
    path('<int:id>/', RoomBookView.as_view()),
]
