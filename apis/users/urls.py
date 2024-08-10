from django.urls import path, include
from rest_framework.routers import SimpleRouter
from apis.users.views import CreateUserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = SimpleRouter()
router.register(r'v1/users', CreateUserViewSet, 'users_v1')

urlpatterns = [
    path('', include(router.urls)),
    path("v1/web-auth/", TokenObtainPairView.as_view(),name='get_token'),
    path("v1/web-auth/refresh", TokenRefreshView.as_view(), name="refresh_token"),
    path("v1/api-auth/", include("rest_framework.urls"))
]