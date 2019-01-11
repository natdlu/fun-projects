import numpy
import random
import datetime

def sum_of_inits(value):
    value = str(value)
    sum = 0
    for i in range(4):
        sum += int(value[i])
    return sum


# Magiczna Kula 8

today = datetime.datetime.now()
sum_of_the_day = today.year + today.month + today.day
sum_of_inits = sum_of_inits(sum_of_the_day)

print(sum_of_inits)