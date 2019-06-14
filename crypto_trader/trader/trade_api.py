from abc import ABC, abstractmethod


class TradeAPI(ABC):
    @abstractmethod
    def get_available_currencies(self):
        pass
