from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r's', views.StudentViewSet)

urlpatterns = [
    # path('',views.home, name='home'),
    # path('list/', views.student_list, name='list'),
    # path('update/<int:id>/', views.update_list, name='update'),
    # path('delete/<int:id>/', views.delete_list, name='delete'),

    path('api/',include(router.urls)),
    path('', views.StudentView.as_view()),
    path('<int:id>/', views.StudentView.as_view()),
]
