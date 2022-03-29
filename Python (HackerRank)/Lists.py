if __name__ == '__main__':
    N = int(input())

    # write your code below here
    arr = []
    for _ in range(N):
        line = input().split()
        if line[0].startswith('i'):  # insert
            arr.insert(int(line[1]), int(line[2]))
        elif line[0].startswith('pr'):  # print
            print(arr)
        elif line[0].startswith('rem') and int(line[1]) in arr:  # remove
            arr.remove(int(line[1]))
        elif line[0].startswith('a'):  # appned
            arr.append(int(line[1]))
        elif line[0].startswith('po'):  # pop
            arr.pop()
        elif line[0].startswith('s'):  # sort
            arr.sort()
        else:  # reverse
            arr = arr[::-1]



