from MyTimer import MyTimer
import datetime


with MyTimer(units='s') as t:
    s = 0
    for i in range(1000000000):
        s += 1


print(t.elapsed_time)