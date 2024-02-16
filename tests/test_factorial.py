import pytest
from src.factorial import factorial

def test_factorial_0():
    assert factorial(0) == 1

def test_factorial_1():
    assert factorial(1) == 1

def test_factorial_5():
    assert factorial(5) == 120

def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_non_integer():
    with pytest.raises(ValueError):
        factorial(1.5)