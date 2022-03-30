# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations


if __name__ == '__main__':
    string, k = input().split()
    k = int(k)
    # print(*permutations(string, k))
    print(*[''.join(i) for i in permutations(sorted(string),k)], sep = '\n')
    # print(lst)