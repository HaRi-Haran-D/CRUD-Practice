from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'viewset', views.StudentViewSet)

urlpatterns = [
    # path('', views.home, name='home'),
    # path('create/', views.CreateStudent.as_view(), name='create'),
    # path('list/', views.StudentList.as_view(), name='list'),
    # path('detail/<int:pk>/', views.StudentDetail.as_view(), name='detail'),
    # path('update/<int:pk>/', views.UpdateStudent.as_view(), name='update'),
    # path('delete/<int:pk>/', views.DeleteStudent.as_view(), name='delete'),


    #Viewset
    path('', include(router.urls)),

    #apiview
    path('api/', views.StudentView.as_view()),
    path('api/<int:id>/', views.StudentView.as_view()),
    path('apiview/', views.create_get_data),
    path('apiview/<int:id>/', views.get_update_delete_by_id),
    path('gene/', views.StudentGenerics.as_view()),
    path('gene/<int:pk>/', views.StudentGenericsByID.as_view()),
]