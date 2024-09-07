# products/urls.py
from django.urls import path
from .views import ProductCreateView, ProductListView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', ProductCreateView.as_view()), 
    path('list/', ProductListView.as_view()),  
    path('<int:pk>/', ProductUpdateView.as_view()),  
    path('<int:pk>/', ProductDeleteView.as_view()),  
]
