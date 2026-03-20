from django.urls import path
from . import views
app_name = 'app'

urlpatterns = [
    path('', views.add, name='add'),
    path('lists/', views.listdata, name='lists'),
    path('update/<int:id>/', views.updatedata, name='update'),
    path('delete/<int:id>/', views.deletedata, name='delete')
]