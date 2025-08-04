from django.urls import path , include
from djoser import views as djoser_views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from rest_framework import routers
from .views import ProfileViewSet

router = routers.DefaultRouter()
router.register(r'profile', ProfileViewSet, basename='profile'),
urlpatterns = [
    path("register/", djoser_views.UserViewSet.as_view({"post": "create"}), name="custom-register"),
    path("login/", TokenObtainPairView.as_view(), name="custom-login"),
    path("refresh/", TokenRefreshView.as_view(), name="custom-refresh"),
    path("logout/", TokenBlacklistView.as_view(), name="custom-logout"),
    path('', include(router.urls)),
]