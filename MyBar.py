from ibapi.wrapper import BarData

class MyBar(BarData):

    def isGreen(self):
        return True if (self.open < self.close) else False

    def isRed(self):
        return True if (self.open > self.close) else False


