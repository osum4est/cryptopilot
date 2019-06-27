"""cryptopilot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers

from server.api import views

router = routers.DefaultRouter()
router.register("traders", views.TraderViewSet)
router.register("currencies", views.CurrencyViewSet)
router.register("candles/download", views.CandlesDownloadViewSet, basename="candles/download")
router.register("candle_overviews", views.CandleOverviewViewSet)
router.register("trade_sessions", views.TradeSessionViewSet)
router.register("price_history", views.PriceHistoryChartView, basename="price_history")

urlpatterns = [
    path('api/', include(router.urls)),

    path('api/admin/', admin.site.urls),

    re_path(r'^(?P<path>.*)/$', views.index_view),
    path('', views.index_view),
]
