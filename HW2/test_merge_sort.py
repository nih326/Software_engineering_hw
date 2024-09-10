"""
This module contains test cases for the merge_sort function
from the hw2_debugging module.
"""

from hw2_debugging import merge_sort

def test_merge_sort_empty():
    """
    Test merge_sort with an empty list. It should return an empty list.
    """
    assert not merge_sort([])  # Simplified by checking if the result is falsey

def test_merge_sort_single_element():
    """
    Test merge_sort with a list containing a single element. It should return the same list.
    """
    assert merge_sort([42]) == [42]

def test_merge_sort_multiple_elements():
    """
    Test merge_sort with a list of multiple elements. It should return a sorted list.
    """
    assert merge_sort([4, 2, 5, 1, 3]) == [1, 2, 3, 4, 5]
