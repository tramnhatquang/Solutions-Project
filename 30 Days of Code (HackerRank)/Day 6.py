import sys

# Enter your code here. Read input from STDIN. Print output to STDOUT


if __name__ == '__main__':
    # num_test = int(input())

    # Using two loops, each loop goes through even or odd indices
    # for i in range(num_test):
    #     line = input()
    #     res = ''
    #     for i in range(0, len(line), 2):
    #         res += line[i]
    #     res += ' '
    #     for i in range(1, len(line), 2):
    #         res += line[i]
    #     print(res)

    # More elegant code
    for i in range(int(input())):
        s = input()
        print(s[::2], s[1::2])