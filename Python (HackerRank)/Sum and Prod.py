import numpy

if __name__ == '__main__':
    n, m = map(int, input().split())
    lst = []
    for i in range(n):
        lst += [list(map(int, input().split()))]

    sum_lst = numpy.sum(lst, axis=0)
    print(numpy.prod(sum_lst))



