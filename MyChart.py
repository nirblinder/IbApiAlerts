from enum import Enum
from MyBar import  MyBar

class MyChart:
    def __init__(self, bar_size):
        self.bar_size = bar_size
        self.barsHistory = [] # no history at init
        self.realTimeBar = MyBar() # init current bar

class MyChartTypesEnum(Enum):
    MIN1 = 1
    MIN5 = 2


