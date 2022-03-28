#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    n = int(input().strip())

    # convert n into a binary number
    count = current = 0
    while n != 0:
        remainder = n % 2
        if remainder == 1:
            current += 1
            if current > count:
                count = current
        else: # update count
            current = 0

        n //= 2

    print(count)


