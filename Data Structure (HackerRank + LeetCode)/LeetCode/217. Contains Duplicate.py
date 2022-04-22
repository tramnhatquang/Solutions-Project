class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # TIme: O(n) when creating a set, len() takes O(1) complexity. Totally, it takes O(n)
        # Space: O(n) since we need to create a set containing all the elements in nums
        return len(set(nums)) != len(nums)

        # Without using built-in functions
        # Time: O(n log n)
        # Space: O(1)
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False