import MyBar


def run(chart):
    if len(chart.bars) > 1:
        if MyBar.isLarger(chart.bars[-2], 0.75) is True and MyBar.isLarger(chart.bars[-1], 0.75) is True and ((MyBar.isGreen(chart.bars[-2]) is True and MyBar.isRed(chart.bars[-1]) is True) or (MyBar.isRed(chart.bars[-2]) is True and MyBar.isGreen(chart.bars[-1]) is True)):
            print(chart.ticker.symbol,  "|", chart.bars[-1].date,  "|", chart.barsize, "engulfing |", str(chart.bars[-1].open))
    else:
        pass
