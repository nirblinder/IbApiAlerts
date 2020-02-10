from MyTicker import MyContract


class MyWatchlist:
    tickers = []
    file = 'watchlist.csv'

    def __init__(self):
        self.importFromFile()

    def importFromFile(self):
        i=0
        with open(self.file, 'r') as f:
            for i, line in enumerate(f):
                params = line.split(',')
                if len(params) != 2:
                    continue
                param_symbol = params[0].lstrip().rstrip()
                param_p_exch = params[1].lstrip().rstrip()
                ticker = MyTicker(i, param_symbol, param_p_exch)
                self.tickers.append(ticker)
                i=i+1

    def print(self):
        for ticker in self.tickers:
            contract.print()
        print('Total: ' + str(len(self.tickers)))

    def getTickers(self):
        return self.tickers
