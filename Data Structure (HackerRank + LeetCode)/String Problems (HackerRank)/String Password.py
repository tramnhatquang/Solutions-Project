def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong

    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"

    count = 0
    if not any([char.isdigit() for char in password]):
        count += 1
    if not any(i.islower() for i in password):
        count += 1
    if not any(i.isupper() for i in password):
        count += 1
    if not any(i in special_characters for i in password):
        count += 1
    return max(count, 6 - n)