from typing import List

# This is the implementation of the selection sort in Python
# Space: O(1)
# Time: O(n^2) worst case, O(n^2) in average case, and O(n^2) in the best case
# Source: AlgoMonster
def selection_sort(unsorted_list: List[int]) -> List[int]:
	n = len(unsorted_list)
	for i in range(n):
		min_index = i
		for j in range(i, n):

			# Finding the index of the smallest element in the unsorted
			# partition
			if unsorted_list[j] < unsorted_list[min_index]:
				min_index = j # update the index if necessary
		# swap the smallest element in the unsorted partition and put it into
		# the next element in the sorted partition
		unsorted_list[i], unsorted_list[min_index] = unsorted_list[min_index], \
		                                             unsorted_list[i]
	return unsorted_list
