import json
import os

cwd = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(cwd, "resources/cryptocurrency-icons/manifest.json")) as f:
    crypto_json = json.loads(f.read())


def get_currency_name(currency):
    global crypto_json
    try:
        return next(c["name"] for c in crypto_json if c["symbol"] == currency)
    except StopIteration:
        return currency


def get_currency_color(currency):
    global crypto_json
    try:
        return next(c["color"] for c in crypto_json if c["symbol"] == currency)
    except StopIteration:
        return "#ffffff"


def get_currency_icon_url(currency):
    try:
        next(c for c in crypto_json if c["symbol"] == currency)
        return "/img/icons/cryptocurrency-icons/" + currency + ".svg"
    except StopIteration:
        return "/img/icons/cryptocurrency-icons/generic.svg"
