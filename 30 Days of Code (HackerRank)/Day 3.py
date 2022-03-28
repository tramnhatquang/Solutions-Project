#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input().strip())

    # write your code below here
    if N & 1:  # check if N is an odd number
        print('Weird')
    else:  # N is even here
        if N in range(6, 21):
            print('Weird')
        else:  # the case is similar when N in [2, 5] and [20, inf]
            print('Not Weird')