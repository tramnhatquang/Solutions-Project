def count_substring(string, sub_string):
    # Approach 1: Using string slicing
    # Time: O(n)
    # Space: O(1)
    # length_sub = len(sub_string)
    # count = 0
    # for i in range(0, len(string)-length_sub+1):
    #     if string[i:i+length_sub] == sub_string:
    #         count += 1
    # return count

    # Approach 2: Using startswith()
    count = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count += 1
    return count


