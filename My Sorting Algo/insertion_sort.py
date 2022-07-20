from typing import List

# This is the implementation of the insertion sort in Python
# Space: O(1)
# Time: O(n^2) worst case, O(n^2) in average case, and O(n) in the best case
# (i.e. in a sorted array)
# Source: AlgoMonster
def insertion_sort(unsorted_list: List[int]) -> List[int]:
	for i in range(1, len(unsorted_list)):
		current = i
		while current > 0 and unsorted_list[current] < unsorted_list[
			current - 1]:
			unsorted_list[current], unsorted_list[current - 1] = unsorted_list[
				                                                     current - 1], \
			                                                     unsorted_list[
				                                                     current]
			current -= 1
	return unsorted_list
