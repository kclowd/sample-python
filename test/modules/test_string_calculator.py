import pytest
from source.string_calculator import string_add

def test_empty_string():
    assert string_add('') == 0
    

def test_single_number():
    assert string_add('4') == 4

def test_two_numbers():
    assert string_add('2,5') == 7

def test_many_numbers():
    assert string_add('3,6,9,12') == 30

def test_one_thousand():
    assert string_add('1,2,1000') == 1003
    
def test_over_thousand():
    assert string_add('1,2,1001') == 3
    
def test_negative_number_exception():
    with pytest.raises(
            ValueError,
            match="Negative numbers are not allowed: -1"
        ):
        string_add("-1")