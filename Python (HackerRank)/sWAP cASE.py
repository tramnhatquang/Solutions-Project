def swap_case(s):
    # Using a traditional for-loop
    # res = ''
    # for char in s:
    #     if char.islower():
    #         res += char.upper()
    #     else:
    #         res += char.lower()
    # return res

    # using the built-in Python function
    # return ''.join(map(str.swapcase, s))

    # using a list comprehension
    return ''.join([i.lower() if i.isupper() else i.upper() for i in s])


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)