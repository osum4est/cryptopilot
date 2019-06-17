from auto_traders.auto_trader import AutoTrader


class TraderTest(AutoTrader):
    def get_id(self):
        return "trader_test"

    def get_name(self):
        return "Test Trader"

    def get_description(self):
        return "Don't actually use this. Trust me."

    def get_version(self):
        return "1.0"

    def run(self):
        pass
