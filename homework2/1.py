from statistics import median
from decimal import Decimal

class MedianFinder:
    def __init__(self):
        self.median_list = []
        

    def addNum(self, number):
        self.median_list.append(number)
    
    def findMedian(self) -> [int]:
        if not self.median_list:
            return Decimal("0")
        else:
            return Decimal("%.5f" % median(self.median_list))


median_finder = MedianFinder()
print(median_finder.findMedian() == 0)

median_finder.addNum(1)
median_finder.addNum(2)
print(median_finder.findMedian() == 1.5)

median_finder.addNum(3)
print(median_finder.findMedian() == 2.)
