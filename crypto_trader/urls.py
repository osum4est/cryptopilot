from django.urls import path

from . import views

urlpatterns = [
    path('download_prices/', views.download_prices, name='download_prices'),
    path('download_prices_progress/', views.download_prices_progress, name='download_prices_progress'),
]