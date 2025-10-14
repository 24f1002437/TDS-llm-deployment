import pytest
from odd_even import classify_numbers

def test_empty_list():
    assert classify_numbers([]) == []

def test_all_odd_numbers():
    assert classify_numbers([1, 3, 5]) == ["odd", "odd", "odd"]

def test_all_even_numbers():
    assert classify_numbers([2, 4, 6]) == ["even", "even", "even"]

def test_mixed_numbers():
    assert classify_numbers([1, 2, 3, 4, 5, 6]) == ["odd", "even", "odd", "even", "odd", "even"]
