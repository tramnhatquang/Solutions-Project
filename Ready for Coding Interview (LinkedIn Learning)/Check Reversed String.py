# Modify the following function:
# Assume both strings have similar length and are not empty
def are_reverses(string_1, string_2):
    # Time: O(n) where n is the length of string_1
    # Space: O(n) since we need to make a copy of the reversed string_2
#     return string_1 == string_2[::-1]

    # Time: O(n) where n is the length of string_1
    # Space: O(1) since we do not use extra variables
    for i in range(len(string_1)):
        if string_1[i] != string_2[len(string_2) - i - 1]:
            return False
    return True

if __name__ == '__main__':
    assert are_reverses('ABC', 'CBA') is True
    assert are_reverses('ABC', 'CBC') is False