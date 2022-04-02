from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # write your code below here
        # Time: O(n).
        # Cons: quite complicated, can be simplify more
        # dic = defaultdict(list)
        # for i in range(len(nums)):
        #     dic[nums[i]].append(i)
        #
        # # print(dic)
        # for key in dic:
        #     second = target - key
        #     if second not in dic:
        #         continue
        #     # second in dic
        #     if second != key:
        #         return dic[key] + dic[second]
        #     else:  # second == key
        #         if len(dic[key]) > 1:
        #             return dic[key]
        #         continue

        # More elegant code: By using enumerate() to get both the index and
        # value
        dic = {}
        for i, val in enumerate(nums):
            second = target - val
            if second in dic:
                return [dic[second], i]
            else:
                dic[val] = i