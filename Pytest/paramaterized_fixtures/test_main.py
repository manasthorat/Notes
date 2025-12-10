from main import is_prime
import pytest

@pytest.mark.parametrize("number, expected", [
    (2, True),
    (3, True),
    (4, False),
    (5, True),
    (10, False),
    (13, True),
    (25, False),
    (29, True),
])

def test_is_prime(number, expected):
    assert is_prime(number) == expected