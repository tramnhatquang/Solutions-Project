from typing import *
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Time: O(n^2) because twoSum takes O(n) and we call it n times where n is the length of nums. Sorting the array takes O(n log n), so overall complexity is O(n^2)
        # Space: from O(log n) to O(n), depending on the implementation of the sorting algorithm

        nums.sort()
        res = []

        for i in range(len(nums)):
            if nums[i] > 0: break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, res, i)

        return res

    def twoSum(self, nums, res, i):
        low, high = i + 1, len(nums) - 1
        while low < high:
            total = nums[low] + nums[i] + nums[high]
            if total < 0:
                low += 1
            elif total > 0:
                high -= 1
            else:  # total == 0
                res.append([nums[low], nums[high], nums[i]])
                low += 1
                high -= 1
                while low < high and nums[low] == nums[low - 1]:
                    low += 1
