class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # brute-force solution, using the built-in functions
        # Time: O(n)
        # Space: O(1) by using an extra set
        # return len(list(set(nums))) != len(nums)

        # Without using built-in functions
        # Time: O(n)
        # Space: O(n)
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                return True
        return False