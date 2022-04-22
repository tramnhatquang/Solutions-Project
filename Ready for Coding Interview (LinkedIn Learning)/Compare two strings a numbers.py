# Remember, you can compare single-character numbers in strings as follows:
# "3" > "1"
# Input:
#  a: The first non-negative integer in string. Example: "123"
#  b: The second non-negative integer in string. Example: "3344"
# Returns:
#  True if a is larger than b.
#  False if a is smaller than or equal to b.

# Time: O(max(n, m)) where n, m is the length of a and b respectively
# Space: O(1)
def larger_than(a, b):
    if len(a) > len(b):
        return True
    elif len(a) < len(b):
        return False

    # in case two strings have similar length
    for i in range(len(a)):
        if a[i] == b[i]:
            continue
        elif a[i] > b[i]:
            return True
        return False
    return False # two strings are equivalent



if __name__ == '__main__':
    assert larger_than('112', '111') is True
    assert larger_than('525', '1111') is False
    assert larger_than('11', '0') is True
    assert larger_than('1', '1') is False

