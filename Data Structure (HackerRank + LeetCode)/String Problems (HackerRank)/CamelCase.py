def camelcase(s):
    # Write your code here
    # Time: O(n) where n is the length of the string
    # Space: O(1)
    count = 1
    for idx, char in enumerate(s):
        if str(char).isupper():
            count += 1
    return count

    # Another elegant solution
    return sum(map(str.isupper, s)) + 1
