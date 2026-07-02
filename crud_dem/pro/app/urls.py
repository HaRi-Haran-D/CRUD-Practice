from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
app_name = 'app'

router = DefaultRouter()
router.register(r'entry', views.TaskView)

urlpatterns = [
    # path('', views.add, name='add'),
    # path('lists/', views.listdata, name='lists'),
    # path('update/<int:id>/', views.updatedata, name='update'),
    # path('delete/<int:id>/', views.deletedata, name='delete')
    path('api/', include(router.urls)),
    path('', views.StudentView.as_view()),
    path('<int:id>/', views.StudentView.as_view()),
    path('task/', views.StudentTaskView.as_view()),
]