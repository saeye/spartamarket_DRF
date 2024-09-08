# products/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProductCreateView.as_view()), 
    path('list/', views.ProductListView.as_view()),  
    path('<int:pk>/', views.ProductUpdateView.as_view()),  
    path('<int:pk>/delete/', views.ProductDeleteView.as_view()),  
]
