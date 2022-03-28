#!/bin/python3

import math
import os
import random
import re
import sys


def bubbleSort(arr) -> None:
    count = 0

    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                count += 1
    # print(arr)
    print(f'Array is sorted in {count} swaps.')
    print('First Element:', arr[0])
    print('Last Element:', arr[-1])


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    # Write your code here
    bubbleSort(a)