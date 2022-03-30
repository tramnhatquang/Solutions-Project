# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

if __name__ == '__main__':
    n = int(input())
    lst = input().split()
    Student = namedtuple('Student', lst)
    total = 0

    for _ in range(n):
        student = Student(*input().split())
        total += int(student.MARKS)

    print(f'{total / n: .2f}')