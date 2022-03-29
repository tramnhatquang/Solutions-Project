if __name__ == '__main__':
    hash_table = {}
    lst = []

    for _ in range(int(input())):
        name = input()
        score = float(input())

        # write your code below here
        # First approach using more variables
        #     hash_table[name] = score

        # second_lowest= sorted(set(hash_table.values()))[1]
        # lst_second_lowest = []
        # for key in hash_table:
        #     if hash_table[key] == second_lowest:
        #         lst_second_lowest.append(key)
        # print('\n'.join(sorted(lst_second_lowest)))

        # Second approach: Using list comprehension
        # Credit: gkeswani92 (HackerRank account: https://www.hackerrank.com/gkeswani92)
        lst.append([name, score])
    second_lowest = sorted(list(set([score for name, score in lst])))[1]
    print('\n'.join([a for a, b in sorted(lst) if b == second_lowest]))

