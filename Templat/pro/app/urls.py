from django.urls import path, include
from . import views
from django.views.decorators.cache import cache_page
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
app_name = 'app'

router = DefaultRouter()
router.register(r"items", views.ItemViewSet, basename='item')
urlpatterns = [
    # path('', views.IndexClassView.as_view(), name='home'),
    path('', views.home, name='home'),
    # path('<int:pk>/', views.FoodDetailView.as_view(), name='detail'),
    path('<int:id>/', views.detail, name='detail'),
    # path('create/', views.ItemCreateView.as_view(), name='create'),
    path('create/',views.create, name='create'),
    path('update/<int:pk>/', views.ItemUpdateView.as_view(), name='update'),
    # path('delete/<int:pk>/', views.ItemDeleteView.as_view(), name='delete'),
    path('delete/<int:id>/', views.delete_item, name='delete'),

    #API URL by DRF
    # path('api/items/', views.ItemListCreateAPI.as_view(), name='api_items'),
    # path('api/items/<int:pk>/', views.ItemRetrieveUpdateDestryAPIView.as_view(), name='get_api_item'),
    path("api/", include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
