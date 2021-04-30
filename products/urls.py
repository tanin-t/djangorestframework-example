
from django.urls import path
from . import views

urlpatterns = [
    path('product/', views.ProductListAPI.as_view()),
    path('product/<int:pk>/', views.ProductDetailAPI.as_view())
]