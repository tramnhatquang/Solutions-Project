# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter

if __name__ == '__main__':
    num_of_shoes = int(input())

    lst_shoes = Counter(map(int, input().split()))
    num_of_customers = int(input())

    total = 0
    # get customers'info
    for i in range(num_of_customers):
        size, price = map(int, input().split())
        if size in lst_shoes and lst_shoes[size] > 0:
            total += price
            lst_shoes[size] -= 1
    print(total)