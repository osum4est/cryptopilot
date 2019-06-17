from django.urls import path

from . import views

urlpatterns = [
    path('download_prices/', views.download_prices, name='download_prices'),
    path('download_prices_progress/', views.download_prices_progress, name='download_prices_progress'),

    path('get_available_data/', views.get_available_data, name='get_available_data'),
    path('get_available_traders/', views.get_available_traders, name='get_available_traders'),

    path('get_price_history_graph/<str:c_id>/<str:length>/', views.PriceHistoryGraphView.as_view(),
         name='get_price_history_graph'),
]
