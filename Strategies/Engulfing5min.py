import MyBar
from Strategies import BarPatterns
from datetime import datetime,timedelta



def run(chart):
    if len(chart.bars) > 2:
        bar_last = chart.bars[-2]
        bar_last_last = chart.bars[-3]
        if MyBar.body_size_percent(bar_last_last) > 0.75 and BarPatterns.body_bigger(bar_last, bar_last_last) is True and (BarPatterns.green_red(bar_last, bar_last_last) is True or BarPatterns.red_green(bar_last, bar_last_last) is True):
            print(chart.ticker.symbol,  "|", str(datetime.strptime(bar_last.date, '%Y%m%d %H:%M:%S')-timedelta(hours=7)),  "|", chart.barsize, "engulfing")
        else:
            pass
    else:
        pass
