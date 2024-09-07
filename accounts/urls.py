from django.urls import path
from .views import SignupView, SigninView, SignoutView, ProfileView

urlpatterns = [
    path("signup/", SignupView.as_view()),
    path("signin/", SigninView.as_view()),
    path("signout/", SignoutView.as_view()),
    path("profiles/<str:username>/", ProfileView.as_view()),
]
