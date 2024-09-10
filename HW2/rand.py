"""
This module contains functions for generating random numbers.
"""
import subprocess


def random_array(arr):
    """
    Fill the input array with random numbers between 1 and 20.

    Args:
        arr (list): A list of integers to be filled with random numbers.

    Returns:
        list: The modified list with random numbers.
    """
    shuffled_num = None
    for i, _ in enumerate(arr):
        shuffled_num = subprocess.run(
            ["shuf", "-i1-20", "-n1"], capture_output=True,check=True)
        arr[i] = int(shuffled_num.stdout)
    return arr
