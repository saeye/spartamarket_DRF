from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
TokenRefreshView,
)

urlpatterns = [
    path("signup/", views.SignupView.as_view()),
    path("signin/", views.SigninView.as_view()),
    path("signout/", views.SignoutView.as_view()),
    path("profiles/<str:username>/", views.ProfileView.as_view()),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
