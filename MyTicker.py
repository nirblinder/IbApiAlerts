from ibapi.contract import Contract
from MyChart import MyChart


class MyTicker(Contract):
    def __init__(self, id, symbol, primaryExchange):
        Contract.__init__(self)
        self.id = id
        self.symbol = symbol
        self.secType = 'STK'
        self.exchange = 'SMART'
        self.primaryExchange = primaryExchange
        self.chart1min = MyChart(1);
        self.chart5min = MyChart(5);

    def print(self):
        print(self.symbol + ", " + self.primaryExchange)

