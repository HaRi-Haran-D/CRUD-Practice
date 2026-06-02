from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home, name='home'),
    # path('list/', views.emp_list, name='list'),
    # path('update/<int:item_id>/', views.update_list, name='update'),
    # path('delete/<int:item_id>/', views.delete_list, name='delete'),
    path('', views.CompanyAPI.as_view(), name='api'),
    path('<int:id>/', views.CompanyAPIByID.as_view(), name='with_id')
]