if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Brute-force solution:
    # Time: O(n^3)
    # Space: O(n)
    # lst = []
    # for i in range(x + 1):
    #     for j in range(y + 1):
    #         for k in range(z + 1):
    #             if i + j + k != n:
    #                 lst.append([i, j, k])
    # print(lst)

    # Using list comprehension
    print([[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a + b+ c != n])