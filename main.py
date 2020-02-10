from ibapi.client import EClient
from ibapi.wrapper import EWrapper
from ibapi.ticktype import TickTypeEnum
from datetime import datetime
from MyWatchlist import  MyWatchlist


class MainApp(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

    def error(self, reqId, errorCode, errorString):
        #pass
        print("Error: ", reqId, " ", errorCode, " ", errorString)

    def historicalData(self, reqId, bar):
        print("historicalData ", reqId, " Date: ", bar.date, "Open: ", bar.open, "Close: ", bar.close, "Low: ", bar.low, "High: ", bar.high, "Volume: ", bar.volume)

    def historicalDataUpdate(self, reqId, bar):
        print("historicalUpdate ", reqId, " Date: ", bar.date, "Open: ", bar.open, "Close: ", bar.close, "Low: ", bar.low, "High: ", bar.high, "Volume: ", bar.volume)

    def historicalDataEnd(self, reqId, startDate, endDate):
        pass
        #print("historicalDataEnd - "+str(reqId)+" from "+startDate+" to "+endDate)

    def currentTime(self, time):
        print(datetime.fromtimestamp(time))

    def tickPrice(self, reqId, tickType, price, attrib):
        if TickTypeEnum.to_str(tickType) == "LAST":
            print("Tick Price. Ticker Id:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "Price:", price)

    def tickSize(self, reqId, tickType, size):
        if TickTypeEnum.to_str(tickType) == "LAST_SIZE":
            print("Tick Size. Ticker Id:", reqId, "tickType:", TickTypeEnum.to_str(tickType), "Size:", size)

    def realtimeBar(self, reqId, date, open, high, low, close, volume, WAP, count):
        print("Real-time Bar. Ticker Id:", reqId, "date:", datetime.fromtimestamp(date), "Close:", close, "Volume:", volume)
        # updateTicker

def main():
    # create watchlist from csv file
    watch_1 = MyWatchlist()

    app = MainApp()
    app.connect("127.0.0.1", 4001, 0)

    for ticker in watch_1.getTickers():
        app.reqRealTimeBars(ticker.id, ticker, 0, "TRADES", 0, [])

    app.run()

if __name__ == "__main__":
    main()