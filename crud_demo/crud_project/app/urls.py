from django.urls import path
from . import views
app_name = 'app'

urlpatterns = [
    path('index/',views.index, name='index'),
    path('listitem/', views.listitem, name='listitem'),
    path('updateform/<int:id>/', views.updateform, name='updateform'),
    path('deleteitem/<int:id>/', views.deleteitem, name='deleteitem')
]
