# test_main.py

import pytest
from main import is_prime

def test_is_prime_pass():
    assert is_prime(5) == True  # This should pass

def test_is_prime_fail():
    assert is_prime(8) == True  # This should fail, as 4 is not a prime number
