# Enter your code here. Read input from STDIN. Print output to STDOUT

def calculateFine(a, b):
    fine = 0
    if a[2] == b[2]:
        if a[1] == b[1] and a[0] > b[0]:
            fine = 15 * (a[0] - b[0])
        elif a[1] > b[1]:
            fine = 500 * (a[1] - b[1])
        # else the book is
    elif a[2] > b[2]:
        fine = 10000
    # else the book is returned earlier than 1+ year expected
    return fine


if __name__ == '__main__':
    returned_day, returned_month, returned_year = map(int, input().split())
    due_day, due_month, due_year = map(int, input().split())
    print(calculateFine([returned_day, returned_month, returned_year],
                        [due_day, due_month, due_year]))
