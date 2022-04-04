#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


#
# Complete the 'birthdayCakeCandles' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY candles as parameter.
#

def birthdayCakeCandles(candles):
    # Write your code here
    # using a Counter object
    # count = 0
    # counter = Counter(candles)
    # for candle in candles:
    #     if counter[candle] > count:
    #         count = counter[candle]
    # return count
    # print(candles.count(max(candles)))

    # Using a built-in function
    return candles.count(max(candles))

