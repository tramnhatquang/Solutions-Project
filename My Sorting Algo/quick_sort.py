from typing import List

# This is the implementation of the quick sort in Python
# Space: O(log n)
# Time: O(n log n) for best, average. O(n^2) for the worst case
# Source: AlgoMonster
def sort_list_interval(unsorted_list: List[int], start: int, end: int) -> None:
    if end - start <= 1:
        return

    # pick the pivot at the last element in the interval
    pivot = unsorted_list[end - 1]
    start_ptr = start
    end_ptr = end - 1
    while start_ptr < end_ptr:
        while unsorted_list[start_ptr] < pivot and start_ptr < end_ptr:
            start_ptr += 1
        while unsorted_list[end_ptr] >= pivot and start_ptr < end_ptr:
            end_ptr -= 1
        if start_ptr == end_ptr:
            break
        unsorted_list[start_ptr], unsorted_list[end_ptr] = unsorted_list[end_ptr], unsorted_list[start_ptr]
    unsorted_list[start_ptr], unsorted_list[end - 1] = unsorted_list[end - 1], unsorted_list[start_ptr]
    sort_list_interval(unsorted_list, start, start_ptr)
    sort_list_interval(unsorted_list, start_ptr + 1, end)

def quick_sort(unsorted_list: List[int]) -> List[int]:
    sort_list_interval(unsorted_list, 0, len(unsorted_list))
    return unsorted_list