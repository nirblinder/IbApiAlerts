from MyTicker import MyTicker
from datetime import datetime

class MyChart:

    def __init__(self, id, barsize, ticker):
        self._id = id
        self._barsize = barsize
        self._ticker = ticker
        self._bars = []
        self.last_minute = -1

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
        # get minute of current bar
        curr_minute = datetime.strptime(bar.date, '%Y%m%d %H:%M:%S').minute

        # if current bar minute is different than last bar, append the current bar
        # otherwise, update the last bar
        if curr_minute != self.last_minute:
            self._bars.append(bar)
        else:
            self._bars[-1] = bar

        self.last_minute = curr_minute


