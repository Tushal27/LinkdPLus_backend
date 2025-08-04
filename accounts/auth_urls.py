from django.urls import path , include
from djoser import views as djoser_views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from .views import PasswordResetView
from .views import ProfileView

urlpatterns = [
    path("register/", djoser_views.UserViewSet.as_view({"post": "create"}), name="custom-register"),
    path("login/", TokenObtainPairView.as_view(), name="custom-login"),
    path("refresh/", TokenRefreshView.as_view(), name="custom-refresh"),
    path("logout/", TokenBlacklistView.as_view(), name="custom-logout"),
    path("reset-password/", PasswordResetView.as_view(), name="password_reset"),
    path('profile/', ProfileView.as_view(), name='profile'),
]