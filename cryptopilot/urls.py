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
from django.urls import path, include
from django.views.generic import RedirectView

from cryptopilot import views

urlpatterns = [
    path('', RedirectView.as_view(url="dashboard/")),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('simulation/', views.simulation, name="simulation"),
    path('simulate/<str:trader_id>/', views.simulate, name="simulate"),
    path('data_loader/', views.data_loader, name="data_loader"),

    path('trader/', include('crypto_trader.urls'))
]
