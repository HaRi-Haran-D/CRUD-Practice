from django.urls import path
from . import views

urlpatterns = [
    # path('',views.home, name='home'),
    # path('list/',views.list, name='list'),
    # path('update/<int:item_id>/', views.update, name='update'),
    # path('delete/<int:item_id>/', views.delete, name='delete')

    path('', views.StudentAPIView.as_view()),
    path('<int:id>/', views.StudentAPIView.as_view()),
    path('teach/', views.create_get_view),
    path('teach/<int:id>/', views.get_update_delete_data),
]
