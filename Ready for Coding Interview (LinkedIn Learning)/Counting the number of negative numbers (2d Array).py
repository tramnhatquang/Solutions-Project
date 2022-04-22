# Problem: Counting the number of negative numbers.¶
# You are given a 2-dimensional array with integers.
#
# Example Input:
# [[-4, -3, -1, 1],
#  [-2, -2, 1, 2],
#  [-1,  1,  2, 3],
#  [ 1,  2,  4, 5]]
#
# Write a function, count_negatives(input), which finds and returns the number of negative integers in th array.

# Input: A 2-dimensional array with integers.  Example below.
# [[-4, -3, -1, 1],
# [-2, -2,  1, 2],
# [-1,  1,  2, 3],
# [ 1,  2,  4, 5]]
# Returns:
#  The number of negative numbers in the array.
#  In the above case, this function should return 6
#  since there are 6 negative numbers in the array.

# The 2d array is always a square one
def count_negatives(given_array):
    # Brute force solution
    # Time: O(n^2) where n is the length of row
    # Space: O(1)
    # count = 0
    # for row in range(len(given_array)):
    #     for col in range(len(given_array[0])):
    #         if given_array[row][col] < 0:
    #             count += 1
    # return count

    # O(n) solution
    count = 0
    row_i = 0
    col_i = len(given_array) - 1
    while col_i >= 0 and row_i < len(given_array):
        if given_array[row_i][col_i] < 0:
            count += col_i + 1
            row_i += 1
        else:
            col_i -= 1
    return count
if __name__ == '__main__':
    assert count_negatives(
        [[-4, -3, -1, 1],
         [-2, -2, 1, 2],
         [-1, 1, 2, 3],
         [1, 2, 4, 5]]) == 6

    assert count_negatives(
        [[-1, 0],
         [0, 0]]) == 1

    assert count_negatives(
        [[-2, 0],
         [-1, 0]]) == 2

    assert count_negatives([[0]])  == 0
