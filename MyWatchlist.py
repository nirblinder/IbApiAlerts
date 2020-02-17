from MyTicker import MyTicker

class MyWatchlist:
    file = 'watchlist.csv'

    def __init__(self):
        self._tickers = []
        self.importFromFile()

    def importFromFile(self):
        with open(self.file, 'r') as f:
            for i, line in enumerate(f):
                params = line.split(',')
                if len(params) != 2:
                    continue
                param_symbol = params[0].lstrip().rstrip()
                param_p_exch = params[1].lstrip().rstrip()
                ticker = MyTicker(i, param_symbol, param_p_exch)
                self._tickers.append(ticker)

    def print(self):
        for ticker in self._tickers:
            ticker.print()
        print('Total: ' + str(len(self._tickers)))

    @property
    def tickers(self):
        return self._tickers
