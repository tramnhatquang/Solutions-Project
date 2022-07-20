from typing import List
from collections import defaultdict


def group_anagrams(strs: List[str]) -> List[List[str]]:
	# WRITE YOUR BRILLIANT CODE HERE
	# Time: O(nm) where n is the length of the list, m is the maximum length of a string
	# Space: O(nm) the total storage we need
	hash_table = defaultdict(list)
	for string in strs:
		count = [0] * 26
		for char in string:
			count[ord(char) - ord('a')] += 1
		hash_table[tuple(count)].append(string)

	return list(hash_table.values())

