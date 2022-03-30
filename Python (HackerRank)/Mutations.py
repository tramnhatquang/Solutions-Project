def mutate_string(string, position, character):
    # Frist approach: Using a substring
    # return string[:position] + character + string[position+1:]

    # Second approach: converting to a list and then modify the character at that given index
    lst = list(string)
    lst[position] = character
    return ''.join(lst)


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)