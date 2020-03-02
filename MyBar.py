

def is_green(bar):
    return True if (bar.open < bar.close) else False


def is_red(bar):
    return True if (bar.open > bar.close) else False


def is_larger(bar, percent):
    return True if (abs(bar.open-bar.close)/bar.open*100 > percent) else False


def body_size_percent(bar):
    return abs(bar.open-bar.close)/bar.open*100


def body_size(bar):
    return abs(bar.open-bar.close)


