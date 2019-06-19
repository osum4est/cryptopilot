# from datatableview.views import DatatableView, Datatable
import json

from django.shortcuts import render

from server.auto_traders.auto_trader import get_auto_traders
from server.crypto_trader.views import TradeSessionsTableView, TradersTableView, AvailableDataTableView


def dashboard(request):
    return render(request, 'cryptopilot/../../templates/cryptopilot/dashboard.html')


def traders(request):
    return render_with_columns(request, 'cryptopilot/traders.html', TradersTableView())


def trade_sessions(request, trader_id):
    return render_with_columns(request, 'cryptopilot/trade_sessions.html', TradeSessionsTableView(), {
        "trader_id": trader_id,
        "trader_name": next(t for t in get_auto_traders() if t.get_id() == trader_id).get_name(),
    })


def data_loader(request):
    return render_with_columns(request, 'cryptopilot/data_loader.html', AvailableDataTableView())


def render_with_columns(request, template_name, datatable, context=None):
    if context is None:
        context = {}
    context["columns"] = json.dumps(datatable.get_column_names())
    return render(request, template_name, context)
