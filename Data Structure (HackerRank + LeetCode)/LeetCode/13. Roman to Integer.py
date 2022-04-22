class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC': 90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }
        # Time: O(1) since we have a finite set of roman numericals
        # Space: O(1) because we use a constant number of single-value variables

        ans = dic.get(s[-1])
        for i in range(len(s) - 2, -1, -1):
            if dic[s[i]] < dic[s[i+1]]:
                ans -= dic[s[i]]
            else:
                ans += dic[s[i]]
        return ans