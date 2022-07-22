#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

def noPrefix(words):
    # Write your code here
    wordDict = {}
    for word in words:
        temp = wordDict
        for letter in word:
            flag=False
            if letter in temp:
                flag = True
                temp = temp[letter]
                if len(temp.keys()) == 0:
                    break
                continue
            temp[letter] = {}
            temp = temp[letter]
        if flag:
            print("BAD SET")
            print(word)
            return
    print("GOOD SET")
if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
