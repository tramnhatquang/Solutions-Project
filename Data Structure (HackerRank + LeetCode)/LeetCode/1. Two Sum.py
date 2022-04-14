class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Time: O(n) where n is the length of the list
        # Space: O(n) since we use the hash_map to store n elements in the given list
        hash_map = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hash_map:
                return [i, hash_map[complement]]
            hash_map[nums[i]] = i