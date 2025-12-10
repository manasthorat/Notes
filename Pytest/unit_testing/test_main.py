import pytest
from main import add, subtract, multiply, divide


# -------------------------
# Tests for add()
# -------------------------

def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_add_mixed_numbers():
    assert add(-2, 3) == 1


# -------------------------
# Tests for subtract()
# -------------------------

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2


def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2


def test_subtract_mixed_numbers():
    assert subtract(5, -3) == 8


# -------------------------
# Tests for multiply()
# -------------------------

def test_multiply_positive_numbers():
    assert multiply(4, 3) == 12


def test_multiply_negative_numbers():
    assert multiply(-4, 3) == -12


def test_multiply_by_zero():
    assert multiply(10, 0) == 0


# -------------------------
# Tests for divide()
# -------------------------

def test_divide_positive_numbers():
    assert divide(10, 2) == 5


def test_divide_negative_numbers():
    assert divide(-10, 2) == -5


def test_divide_float_result():
    assert divide(7, 2) == 3.5


def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(10, 0)
