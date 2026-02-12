from django.urls import path
from . import views
app_name = 'list'

urlpatterns = [
    path('', views.post, name='post'),
    path('new-post/', views.posts_new, name='new-post'),
    path('<slug:slug>', views.post_list, name='post_list'),
]