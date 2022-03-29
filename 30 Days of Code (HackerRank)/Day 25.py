# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import sqrt


def isPrime(x: int) -> bool:
    # for i in range(2, math.ceil(math.sqrt(x))):
    for i in range(2, int(sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True


if __name__ == '__main__':

    n = int(input())

    for _ in range(n):
        num = int(input())
        if num >= 2 and isPrime(num):
            print('Prime')
        else:
            print('Not prime')