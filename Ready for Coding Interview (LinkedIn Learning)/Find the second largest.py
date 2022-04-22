### NOTE: Feel free to use any other language or any other IDE for solving this problem.

### NOTE 2: Make sure to run your program once you write it.

#### Oh, and most importantly, have fun solving it! :)

# Implement your function below.

# Input:
#  a: The given list/array of integers.  Example: [1, -2, 3, 4]
# Returns:
#  The second largest number in the list or None if
#  the array's length is only 1 or 2.
def second_largest(given_list):
    # Time: O(n log n)
    # Space: O(1)
    #     if len(given_list) < 2:
    #         return None

    #     given_list.sort(reverse = True)
    #     return given_list[1]

    # Time: O(n) where n is list's length
    # Space: O(1)
    # if len(given_list) < 2:
    #     return None
    #
    # second = first = given_list[0]
    # for num in given_list:
    #     if num > first:
    #         second = first
    #         first = num
    #     elif num > second:
    #         second = num
    # return second

    # Instructor's solution:
    second_largest = largest = None

    for num in given_list:
        if largest is None:
            largest = num
        elif num > largest:
            second_largest = largest
            largest = num
        elif second_largest is None:
            second_largest = num
        elif num > second_largest:
            second_largest = num
    return second_largest


# Use the code below to test your function.
if __name__ == '__main__':
    print('The second largest number in [1, 3, 4, 5, 0, 2] is (should be 4):')
    print(second_largest([1, 3, 4, 5, 0, 2]))

    print('The second largest number in [-2, -1] is: (should be -2)')
    print(second_largest([-2, -1]))

    print('The second largest number in [2, 2, 1] is: (should be 2)')
    print(second_largest([2, 2, 1]))

    print('The second largest number in [2] is: (should be None)')
    print(second_largest([2]))

    print('The second largest number in [] is: (should be None)')
    print(second_largest([]))
