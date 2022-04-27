from typing import List


# This is the implementation of the merge sort in Python
# Space: O(n)
# Time: O(n log n) for the best, worst and average cases
# The merge sort is stable because two similar elements will remain their
# relative orders after sorting
# Source: AlgoMonster
def merge_sort(unsorted_list: List[int]) -> List[int]:
        n = len(unsorted_list)
        if n <= 1:
            return unsorted_list
        midpoint = n // 2
        left_list, right_list = merge_sort(unsorted_list[:midpoint]), merge_sort(
            unsorted_list[midpoint:])
        result_list = []
        left_pointer, right_pointer = 0, 0
        while left_pointer < midpoint or right_pointer < n - midpoint:
            if left_pointer == midpoint:
                result_list.append(right_list[right_pointer])
                right_pointer += 1
            elif right_pointer == n - midpoint:
                result_list.append(left_list[left_pointer])
                left_pointer += 1
            elif left_list[left_pointer] <= right_list[right_pointer]:
                result_list.append(left_list[left_pointer])
                left_pointer += 1
            else:
                result_list.append(right_list[right_pointer])
                right_pointer += 1
        return result_list
