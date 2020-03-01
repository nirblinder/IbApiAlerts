# from ibapi.wrapper import BarData


def isGreen(bar):
    return True if (bar.open < bar.close) else False

def isRed(bar):
    return True if (bar.open > bar.close) else False

def isLarger(bar, percent):
    return True if (abs(bar.open-bar.close)/bar.open*100 > percent) else False


