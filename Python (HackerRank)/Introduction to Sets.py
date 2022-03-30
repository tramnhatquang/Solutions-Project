def average(array):
    # your code goes here
    array = list(set(array))
    return round(sum(array) / len(array), 3)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)