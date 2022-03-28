# search target index
from bisect import bisect_left, bisect_right
array = [1, 2, 3, 5, 6, 7]


def binary_search(array, target, start, end):
    if start > end:
        return "타겟이 배열내에 없습니다."
    mid = (start+end)//2
    if array[mid] == target:
        return mid
    if array[mid] > target:
        return binary_search(array, target, start, mid-1)
    if array[mid] < target:
        return binary_search(array, target, mid+1, end)


# count by range


def count_by_range(array, left_value, right_value):
    left_index = bisect_left(array, left_value)
    right_index = bisect_right(array, right_value)
    return right_index-left_index
