from hw2_debugging import merge_sort
def test_merge_sort_empty():
    assert merge_sort([]) == []

def test_merge_sort_single_element():
    assert merge_sort([42]) == [42]

def test_merge_sort_multiple_elements():
    assert merge_sort([4, 2, 5, 1, 3]) == [1, 2, 3, 4, 5]
