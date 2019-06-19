from django.urls import path

from . import views

urlpatterns = [
    path('download_prices/', views.download_prices, name='download_prices'),
    path('download_prices_progress/', views.download_prices_progress, name='download_prices_progress'),

    path('get_available_data/', views.AvailableDataTableView.as_view(), name='get_available_data'),

    path('get_traders_table/', views.TradersTableView.as_view(), name='get_traders_table'),

    path('get_trade_sessions_table/<str:trader_id>', views.TradeSessionsTableView.as_view(),
         name='get_trade_sessions_table'),

    path('get_price_history_graph/<str:c_id>/<str:length>/', views.PriceHistoryGraphView.as_view(),
         name='get_price_history_graph'),
]
