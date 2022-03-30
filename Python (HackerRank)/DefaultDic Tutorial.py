# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import defaultdict

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = defaultdict(list)

    for i in range(n):
        a[input().strip()].append(i + 1)

    for i in range(m):
        char = input().strip()
        if char in a:
            print(' '.join(map(str, a[char])))
        else:
            print(-1)

