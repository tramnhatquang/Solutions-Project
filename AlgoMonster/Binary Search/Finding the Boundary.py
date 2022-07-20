from typing import List


def find_boundary(arr: List[bool]) -> int:
	# WRITE YOUR BRILLIANT CODE HERE
	# Time: O(n), Space: O(1)
	# if True not in arr:
	#    return -1
	# return arr.index(True)

	# Time: O(log n)
	# Space: O(1)
	start, end = 0, len(arr) - 1
	boundary_index = -1

	while start <= end:
		mid = (start + end) // 2
		if arr[mid]:
			boundary_index = mid
			end = mid - 1
		else:
			start = mid + 1
	return boundary_index