from MyTicker import MyTicker
from MyBar import MyBar

class MyChart:
    bar_size = 1
    barsHistory = []

    def __init__(self, bar_size, ticker):
        self.bar_size = bar_size
        self._ticker = ticker

    def update(self, bar):
        pass

    @property
    def ticker(self):
        return self._ticker






