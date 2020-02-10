from ibapi.contract import Contract
from MyChart import MyChart
from MyChart import MyChartTypesEnum
from datetime import datetime

class MyTicker(Contract):
    def __init__(self, id, symbol, primaryExchange):
        Contract.__init__(self)
        self.id = id
        self.symbol = symbol
        self.secType = 'STK'
        self.exchange = 'SMART'
        self.primaryExchange = primaryExchange
        self.chart1min = MyChart(MyChartTypesEnum.MIN1);
        self.chart5min = MyChart(MyChartTypesEnum.MIN5);

    def print(self):
        print(self.symbol + ", " + self.primaryExchange)

    def updateRealTimeBar(self, id, time, open, high, low, close, volume):
        # update 1 min chart

        # update 5 min chart
        pass



        # return 0 if bar closed otherwise return -1

