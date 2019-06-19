from server.auto_traders.auto_trader import AutoTrader


class TraderBasic(AutoTrader):
    def get_id(self):
        return "trader_basic"

    def get_name(self):
        return "Basic Trader"

    def get_description(self):
        return "A basic trader."

    def get_version(self):
        return "1.0"

    def run(self):
        pass
