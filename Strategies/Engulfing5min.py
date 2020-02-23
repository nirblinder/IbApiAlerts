from MyBar import MyBar

class Engulfing5min:

    def __init__(self):
        pass

    def update(self, bar_previous, bar_current):
        if bar_previous.isGreen() is True and bar_current.isRed() is True:
            self.alert()
        else:
            pass

    def alert(self):
        print("5 min engulfing")