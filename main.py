from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from datetime import datetime
from MyWatchlist import MyWatchlist
from MyLayout import MyLayout


class MainApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        pass
        #print("Error: ", reqId, " ", errorCode, " ", errorString)

    def historicalData(self, reqId, bar):
        layout_1.updateChart(reqId, bar)
        #print("historicalData ", reqId, " Date: ", bar.date, "Open: ", bar.open, "Close: ", bar.close, "Low: ", bar.low, "High: ", bar.high, "Volume: ", bar.volume)

    def historicalDataUpdate(self, reqId, bar):
        layout_1.updateChart(reqId, bar)
        #print("historicalUpdate ", reqId, " Date: ", bar.date, "Open: ", bar.open, "Close: ", bar.close, "Low: ", bar.low, "High: ", bar.high, "Volume: ", bar.volume)


def main():
    # create watchlist from csv file
    watch_1 = MyWatchlist()

    # build layout with 1min and 5min charts for each ticker in watchlist
    global layout_1
    layout_1 = MyLayout(watch_1)

    # setup the api app and connect
    app = MainApp()
    app.connect("127.0.0.1", 4001, 0)

    # build duration string in seconds from today's start to now
    # on start-up the charts will populate with data from start of the day
    now = datetime.now()
    start = now.replace(hour=22, minute=30, second=0, microsecond=0)
    duration = int((now-start).total_seconds())
    durationString = str(duration) + " S"

    # request historical and realtime data from all ticker in the watchlist
    for chart in layout_1.charts:
        app.reqHistoricalData(chart.id, chart.ticker, "", durationString, chart.barsize, "TRADES", 0, 1, True, [])

    # run the api app
    app.run()

if __name__ == "__main__":
    main()
