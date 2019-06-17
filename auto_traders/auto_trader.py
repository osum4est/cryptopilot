from abc import ABC, abstractmethod


def get_auto_trader(name):
    return next(t for t in get_auto_traders() if t.get_name() == name)


def get_auto_traders():
    return [t() for t in AutoTrader.__subclasses__()]


class AutoTrader(ABC):
    @abstractmethod
    def get_id(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_description(self):
        pass

    @abstractmethod
    def get_version(self):
        pass

    @abstractmethod
    def run(self):
        pass
