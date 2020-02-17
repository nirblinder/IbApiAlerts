from MyChart import MyChart

class MyLayout:
    charts = []

    def __init__(self):
        pass

    def addChart(self, chart):
        self.charts.append(chart)

    def updateChart(self, chartId, bar):
        pass

    def getNumOfCharts(self):
        return str(len(self.charts))

    def print(self):
        for chart in self.charts:
            print(str(chart.ticker.id) + " " + str(chart.ticker.symbol))
        print('Total: ' + str(len(self.charts)))