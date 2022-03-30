# Enter your code here. Read input from STDIN. Print output to STDOUT

if __name__ == '__main__':
    m = int(input())

    a = set(map(int, input().split()))
    n = int(input())
    b = set(map(int, input().split()))

    lst = []
    lst += list(a.difference(b))
    lst += list(b.difference(a))

    print(*sorted(lst), sep='\n')
