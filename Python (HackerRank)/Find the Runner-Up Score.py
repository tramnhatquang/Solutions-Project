if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    # Approach 1: Using the built-in sorted
    # Time: O(nlogn) due to the built-in timsort
    # Space: O(1)
    # arr = sorted(set(arr), reverse = True)

    # the array has one element which is also the runner-up
    # if len(arr) == 1:
    #     print(arr[0])
    # else:
    #     print(arr[1])

    # Approach 2:
    # Due to the constraint, the min value in array is -100.
    # Time: O(n)
    largest = second_largest = -101
    for i in arr:
        if i > largest:
            second_largest, largest = largest, i
        elif i > second_largest and i != largest:
            second_largest = i
    print(second_largest)