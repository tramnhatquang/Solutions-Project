class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Time: O(n) where n is the length of the string
        # Space (HashMap): O(min(m, n)) where m is the size of the hash table
        #

        ans = 0
        # map stores the current index + 1 of a character
        hash_map = {}
        start = 0
        # try to extend the range [start, end]
        for end, char in enumerate(s):
            if char in hash_map:
                # update the start when we reach a recurring character
                start = max(hash_map[char], start)

            ans = max(ans, end - start + 1)
            hash_map[char] = end + 1

        return ans

