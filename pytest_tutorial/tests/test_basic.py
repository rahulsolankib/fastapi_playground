import pytest
import app.main as funcs

def test_basic():
    assert funcs.divide_two_number(number_one=10, number_two=2) == 5

def test_basic_zero():
    with pytest.raises(ZeroDivisionError):
        funcs.divide_two_number(number_one=10, number_two=0)

def test_basic_string():
    with pytest.raises(TypeError):
        funcs.divide_two_number(number_one="10", number_two=2)

def test_basic_float():
    assert funcs.divide_two_number(number_one=10.0, number_two=2) == 5.0

def test_basic_negative():
    assert funcs.divide_two_number(number_one=-10, number_two=2) == -5

def test_basic_negative_float():
    assert funcs.divide_two_number(number_one=-10.0, number_two=2.1) == -5