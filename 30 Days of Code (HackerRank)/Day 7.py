#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    #
    arr = list(map(int, input().rstrip().split()))
    # res = ''
    # for i in arr[::-1]:
    #     res += str(i) + ' '
    # print(res)

    # Elegant one-liner code
    print(' '.join(map(str, arr[::-1])))

