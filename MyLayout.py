from MyChart import MyChart


class MyLayout:

    def __init__(self, watchlist):
        self._charts = []
        for index, ticker in enumerate(watchlist.tickers):
            self.charts.append(MyChart(index * 2, "1 min", ticker))
            self.charts.append(MyChart(index * 2 + 1, "5 mins", ticker))

    @property
    def charts(self):
        return self._charts

    def updateChart(self, id, bar):
        self._charts[id].update(bar)

    def getNumOfCharts(self):
        return len(self._charts)

    def print(self):
        for chart in self._charts:
            print(str(chart.id) + " | " + str(chart.barsize) + " | " + str(chart.ticker.symbol))
        print('Total: ' + str(len(self._charts)))
