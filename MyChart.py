from MyTicker import MyTicker
from MyBar import MyBar

class MyChart:

    def __init__(self, id, barsize, ticker):
        self._id = id
        self._barsize = barsize
        self._ticker = ticker
        self._bars = []

    @property
    def id(self):
        return self._id

    @property
    def ticker(self):
        return self._ticker

    @property
    def bars(self):
        return self._bars

    @property
    def barsize(self):
        return self._barsize

    def update(self, bar):
        self._bars.append(bar)


