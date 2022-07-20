from collections import *
from typing import *

class Solution:
	def isIsomorphic(self, s: str, t: str) -> bool:
		# Time: O(n) where n is the length of s
		# Space: O(1) since the size of ASCII character set is fixed and
		map_s_t = {}
		used = set()  # contains used values from string t

		for i in range(len(s)):
			if s[i] in map_s_t:
				if map_s_t[s[i]] != t[i]:
					return False
			else:
				if t[i] in used:
					return False
				map_s_t[s[i]] = t[i]
				used.add(t[i])
		return True


	# The follow up question to group the isomorphic strings as well
	# input =  ['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx']
	#
	# output = [
	#          ['xyx',
	#          ['xyz', 'abc', 'def'],
	#          ['aab', 'xxy']
	#          ]
	# Time: O(nm) where n is the length of string, m is the maximum length of
	# string in the list
	# Space: O(n)
	def groupIsomorphic(self, strings):
		def encode(s):
			d = {}
			return tuple([d.setdefault(c, len(d)) for c in s])

		groups = defaultdict(list)
		for s in strings:
			groups[encode(s)].append(s)

		return list(groups.values())

	# def unique_iso_string(self, string: str) -> str:
	# 	seen: Dict[str, str] = {}
	# 	current, key = ord('a'), []
	# 	for char in string:
	# 		if char not in seen:
	# 			seen[char] = chr(current)
	# 			current += 1
	# 		key.append(seen[char])
	# 	return ''.join(key)
	#
	# # O(n) time and space in the size of strings or O(nm) where n = length of
	# # strings, m = length of strings[i]
	# def group_strings(self, strings: List[str]) -> List[str]:
	# 	iso_strings: Dict[str, List[str]] = defaultdict(list)
	# 	for string in strings:
	# 		key = self.unique_iso_string(string)
	# 		iso_strings[key].append(string)
	# 	return list(iso_strings.values())


if __name__ == '__main__':
	s = Solution()
	print(s.groupIsomorphic(['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx']))
	print(s.groupIsomorphic(["apple", "apply", "dog", "cog", "romi"]))

	# print(s.group_strings(['aab', 'xxy', 'xyz', 'abc', 'def', 'xyx']))
	# print(s.group_strings(["apple", "apply", "dog", "cog", "romi"]))