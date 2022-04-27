from typing import List

# This is the implementation of the bubble sort in Python
# Space: O(1)
# Time: O(n^2) worst case, O(n^2) in average case, and O(n) in the best case
# (i.e. in a sorted array)
# Source: AlgoMonster
def bubble_sort(unsorted_list: List[int]) -> List[int]:
	n = len(unsorted_list)
	for i in reversed(range(n)):
		swapped = False
		for j in range(i):
			if unsorted_list[j] > unsorted_list[j + 1]:
				unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], \
				                                         unsorted_list[j]
				swapped = True
		if not swapped:
			return unsorted_list
	return unsorted_list