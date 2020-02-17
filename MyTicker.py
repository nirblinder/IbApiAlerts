from ibapi.contract import Contract

class MyTicker(Contract):
    def __init__(self, id, symbol, primaryExchange):
        Contract.__init__(self)
        self._id = id
        self.symbol = symbol
        self.secType = 'STK'
        self.exchange = 'SMART'
        self.primaryExchange = primaryExchange

    def print(self):
        print(self._symbol + ", " + self._primaryExchange)

    @property
    def id(self):
        return self._id

    def getSymbol(self):
        return self.symbol
