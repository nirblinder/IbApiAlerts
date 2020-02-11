class MyBar:
    def __init__(self, open, low, high, close, volume):
        self.open = open # ?
        self.low = low
        self.high = high
        self.close = close
        self.volume = volume

    def update(self, low, high, close, volume):
        if low < self.low:
            self.low = low
        if high > self.high:
            self.high = high
        self.close = close
        self.volume += volume
