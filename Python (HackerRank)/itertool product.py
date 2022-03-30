# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    print(*product(a, b))