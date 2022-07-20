class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Time: O(n)
        # Space: O(1) because the table's size stays constant no matter how large n is
        if len(s) != len(t):
            return False

        dic1, dic2 = {}, {}
        for i in range(len(s)):
            dic1[s[i]] = 1 + dic1.get(s[i], 0)
            dic2[t[i]] = 1 + dic2.get(t[i], 0)

        return dic1 == dic2

        # TIme: O(n) where n is the length of string s
        # Space: O(1) because the table's size is constant no matter how large n is
        if len(s) != len(t):
            return False

        dic = {}

        for char in s:
            dic[char] = 1 + dic.get(char, 0)

        for char in t:
            if char not in dic:
                return False
            dic[char] -= 1

        for value in dic.values():
            if value != 0:
                return False
        return True