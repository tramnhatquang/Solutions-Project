class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = float('-inf')

    # Add your code here
    def computeDifference(self):
        # use abs() not really necessary here
        # we are dealing with only positive integers
        self.maximumDifference = max(self.__elements) - min(self.__elements)


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)