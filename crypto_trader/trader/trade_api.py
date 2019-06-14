from abc import ABC, abstractmethod


class TradeAPI(ABC):
    @abstractmethod
    def get_available_currencies(self):
        pass

    @abstractmethod
    def get_historic_rates(self, currency_id, start_date, end_date, granularity):
        pass
