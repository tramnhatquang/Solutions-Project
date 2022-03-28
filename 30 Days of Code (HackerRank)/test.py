
def convertDecimalToBinary(num: int) -> int:
    """
    Convert a given decimal number into a binary number
    :param num: the given decimal number
    :return: the corresponding binary number
    """
    a = []
    res = ''
    while num != 0:
        remainder = num % 2
        a.append(remainder)
        num //= 2

    for i in map(str, a[::-1]):
        res += i
    print(res)
    return int(res)


if __name__ == '__main__':
    assert 101 == convertDecimalToBinary(5)
    # assert 0 == convertDecimalToBinary(0)
    assert 1100 == convertDecimalToBinary(12)

