"""Rcursive Binary Search
Given a sorted list and a search value... implement a recursive binary search
the output should be the index of the search value if it's in the list
or None otherwise."""


def binary_recursive(arr, key, l, h):
    h = len(arr) - 1
    if l > h:
        return None
    mid = l + (h - l) // 2
    if key == arr[mid]:
        return mid
    elif key < arr[mid]:
        return binary_recursive(arr, key, l, mid - 1)
    else:
        return binary_recursive(arr, key, mid + 1, h)


assert binary_recursive([2, 3, 5, 6, 7, 9, 10], 0, 10) == 6
assert binary_recursive([2, 3, 7, 7, 7, 9, 10], 7) == 3
assert binary_recursive([5, 6, 8, 9, 10], 5) == 0
assert binary_recursive([2, 3, 10], 7) == None
assert binary_recursive([4, 5, 5, 7, 8, 9, 10], 10) == 6
# assert binary_recursive([2, 3, 4, 7, 7, 9, 10, 11, 11, 11], 11) == 8
assert binary_recursive([], 3) == None
assert binary_recursive(
    [1, 1, 1, 1, 1, 1, 1, 2, 3, 7, 8, 9, 10, 11, 12], 1) == 3
assert binary_recursive(
    [1, 2, 3, 7, 7, 9, 9, 9, 9, 9, 9, 9, 9, 10, 11], 9) == 7
assert binary_recursive([9, 9, 9, 9, 9, 9, 9, 9, 9, 9,
                         9, 9, 9, 9, 9, 9, 9, 9], 9) == 9
