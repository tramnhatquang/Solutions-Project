from typing import List


def binary_search(arr: List[int], target: int) -> int:
	# WRITE YOUR BRILLIANT CODE HERE
	start, end = 0, len(arr) - 1
	while start <= end:
		mid = (start + end) // 2
		if target == arr[mid]:
			return mid  # bingo, we found the result
		elif arr[mid] < target:
			start = mid + 1
		else:
			end = mid - 1
	return -1
