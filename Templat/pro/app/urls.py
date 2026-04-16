from django.urls import path
from . import views


app_name = 'app'
urlpatterns = [
    path('', views.IndexClassView.as_view(), name='home'),
    # path('', views.home, name='home'),
    path('<int:pk>/', views.FoodDetailView.as_view(), name='detail'),
    # path('<int:id>/', views.detailview, name='detail'),
    path('create/', views.ItemCreateView.as_view(), name='create'),
    # path('create/',views.create, name='create'),
    path('update/<int:pk>/', views.ItemUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/', views.ItemDeleteView.as_view(), name='delete'),
    path('delete/<int:id>/', views.delete_item, name='delete'),
]
