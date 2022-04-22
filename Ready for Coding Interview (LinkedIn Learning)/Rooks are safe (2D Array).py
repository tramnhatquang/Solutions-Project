# Problem: Can rooks attack one another?
# You are given a configuration of a chessboard with rooks in a 2 dimensional array.
#
# Example Input:
# [[1, 0, 0, 0],
# [0, 1, 0, 0],
# [0, 0, 0, 1],
# [0, 0, 0, 0]]
#
# 1 represents that a rook is in the corresponding space on the board, and 0 represents that there's nothing there.
#
# Remember, rooks are able to move horizontally and vertically over any number of spaces.
#
# Write a function, rooks_are_safe(input) which returns True if none of the rooks can attack each other.

# Input:
#  chessboard: A 2-dimensional array that represents.  Example below.
#  [[1, 0, 0, 0],
#  [0, 1, 0, 0],
#  [0, 0, 0, 1],
#  [0, 0, 0, 0]]
# Returns:
#  True if none of the rooks can attack each other.
#  False if there is at least one pair of rooks that can attack each other.
def rooks_are_safe(chessboard):
    # Time: O(n^2)
    # Space: O(1)
    n = len(chessboard)

    for row_idx in range(n):
        count = 0
        for col_idx in range(n):
            count += chessboard[row_idx][col_idx]
        if count > 1:
            return False

    for col_idx in range(n):
        count = 0
        for row_idx in range(n):
            count += chessboard[row_idx][col_idx]
        if count > 1:
            return False
    return True


if __name__ == '__main__':
    assert rooks_are_safe(
        [[1, 0, 0, 0],
         [0, 1, 0, 0],
         [0, 0, 0, 1],
         [0, 0, 0, 0]]) is True
    assert rooks_are_safe([[1]]) is True
    assert rooks_are_safe(
        [[1, 0],
         [1, 0]]) is False
    assert rooks_are_safe(
        [[0, 0, 0],
         [1, 0, 1],
         [0, 0, 0]]) is False
