from enum import Enum

class MyChart:
    def __init__(self, bar_size):
        self.bar_size = bar_size
        self.bars = []

class MyChartTypesEnum(Enum):
    MIN1 = 1
    MIN5 = 2

