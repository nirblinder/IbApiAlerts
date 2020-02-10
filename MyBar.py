class MyBar:
    def __init__(self, time, open, low, high, close, volume):
        self.time = time
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
