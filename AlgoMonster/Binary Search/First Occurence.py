from typing import List


def find_first_occurrence(arr: List[int], target: int) -> int:
	# WRITE YOUR BRILLIANT CODE HERE
	# Time: O(n), Space: O(1)
	# return arr.index(target) if target in arr else -1

	# We can do better by using binary search
	# Time: O(log n)
	# Space: O(1)
	l, r = 0, len(arr) - 1
	ans = -1
	while l <= r:
		mid = (l + r) // 2

		if arr[mid] == target:
			ans = mid
			r = mid - 1
		elif arr[mid] > target:
			r = mid - 1
		else:
			l = mid + 1
	return ans
