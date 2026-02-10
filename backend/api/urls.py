from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    DatasetViewSet,
    register_user,
    login_user,
    logout_user,
    current_user
)

router = DefaultRouter()
router.register(r'datasets', DatasetViewSet, basename='dataset')

urlpatterns = [
    # Authentication endpoints
    path('auth/register/', register_user, name='register'),
    path('auth/login/', login_user, name='login'),
    path('auth/logout/', logout_user, name='logout'),
    path('auth/user/', current_user, name='current-user'),
    
    # Router URLs
    path('', include(router.urls)),
]
