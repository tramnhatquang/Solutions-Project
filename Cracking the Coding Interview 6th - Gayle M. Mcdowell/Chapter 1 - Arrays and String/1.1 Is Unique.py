def is_unique(string: str) -> bool:
    return len(set(str)) == len(str)


def is_unique_chars_algorithmic(string):
    if len(string) > 128:
        return False

        # this is a pythonic and faster way to initialize an array with a fixed value.
        #  careful though it won't work for a doubly nested array
    char_set = [False] * 128
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True


if __name__ == '__main__':
    pass