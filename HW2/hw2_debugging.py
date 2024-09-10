"""
This module implements the merge sort algorithm.
It includes functions to recursively sort an array and merge two sorted arrays.
"""
import rand

def merge_sort(array):
    """
    Recursively sorts an array using the merge sort algorithm.
    Args:
        array (list): The list of elements to be sorted.
    Returns:
        list: A new list that is sorted in ascending order.
    """
    if len(array) == 1:
        return array

    half = len(array) // 2

    return recombine(merge_sort(array[:half]), merge_sort(arr[half:]))


def recombine(left_arr, right_arr):
    """
     Merges two sorted arrays into a single sorted array.

    Args:
        left_arr (list): The left half of the sorted array.
        right_arr (list): The right half of the sorted array.

    Returns:
        list: A merged and sorted array containing all elements from left_arr and right_arr.
    """
    left_index = 0
    right_index = 0
    merge_arr = [None] * (len(left_arr) + len(right_arr))
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            right_index += 1
            merge_arr[left_index + right_index] = left_arr[left_index]
        else:
            left_index += 1
            merge_arr[left_index + right_index] = right_arr[right_index]

     # Add remaining elements from right_arr
    for i in range(right_index, len(right_arr)):
        merge_arr[left_index + right_index] = right_arr[i]

     # Add remaining elements from left_arr
    for i in range(left_index, len(left_arr)):
        merge_arr[left_index + right_index] = left_arr[i]

    return merge_arr


arr = rand.random_array([None] * 20)
arr_out = merge_sort(arr)

print(arr_out)
