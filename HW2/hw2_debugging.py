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
    # Base case: if the array is empty or has one element, return it as is
    if len(array) <= 1:
        return array

    half = len(array) // 2

    # Recursively sort both halves and combine them
    return recombine(merge_sort(array[:half]), merge_sort(array[half:]))

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
    merge_arr = []

    # Compare elements from both arrays and build the merged array
    while left_index < len(left_arr) and right_index < len(right_arr):
        if left_arr[left_index] < right_arr[right_index]:
            merge_arr.append(left_arr[left_index])
            left_index += 1
        else:
            merge_arr.append(right_arr[right_index])
            right_index += 1

    # If there are remaining elements in left_arr, add them
    while left_index < len(left_arr):
        merge_arr.append(left_arr[left_index])
        left_index += 1

    # If there are remaining elements in right_arr, add them
    while right_index < len(right_arr):
        merge_arr.append(right_arr[right_index])
        right_index += 1

    return merge_arr

# Sample random array generation (make sure rand.random_array is defined)
arr = rand.random_array([None] * 20)  # Ensure this generates a valid array
arr_out = merge_sort(arr)

print(arr_out)
