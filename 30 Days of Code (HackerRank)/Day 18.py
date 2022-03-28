import sys


class Solution:
    # Write your code here
    def __init__(self):
        self.arr = []

    def pushCharacter(self, num) -> None:
        self.arr.append(num)

    def popCharacter(self) -> int:
        return self.arr.pop()

    def enqueueCharacter(self, num) -> None:
        self.arr.append(num)

    def dequeueCharacter(self) -> int:
        return self.arr.pop(0)


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break
# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")