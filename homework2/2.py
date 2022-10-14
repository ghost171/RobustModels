import datetime
from decimal import Decimal

class MyTimer:
    def __init__(self, units='s'):
        self.spent_time = 0
        self.start_time = 0
        self.end_time = 0
        self.units = units

    def __enter__(self):
        self.start_time = datetime.datetime.now()
        return self
    
    def __exit__(self, exc_type, exc_value, tb):
        self.end_time = datetime.datetime.now()
        diff_time = self.end_time - self.start_time
        if self.units == 'm':
            self.spent_time = Decimal("%.2f" % (diff_time.total_seconds() / 60))
        elif self.units == 's':
            self.spent_time = int(diff_time.total_seconds())
        elif self.units == 'h': 
            self.spent_time = Decimal("%.2f" % (diff_time.total_seconds() / 60 / 60))
        else:
            print("Argument units has to contain only values of 'm', 's' or 'h'")
            exit(0)

    def elapsed_time(self):
        return self.spent_time
    

if __name__ == "__main__":
    with MyTimer(units='s') as t:
        s = 0
        for i in range(1000000000):
            s += 1

    print(t.elapsed_time())