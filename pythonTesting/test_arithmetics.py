from arithmetics import add, divide
import pytest

def test_add_two_positive_numbers():
    result = add(1, 4)
    assert result == 5

def test_add_two_fail_intensionally():
    result = add(1, 4)
    assert result == 900

def test_add_negative():
    assert add(-1, -4) == -5

def test_add_multisign():
    assert add(1, -4) == -3
    assert add(3, -2) == 0


def test_div_positive():
    assert  divide(15, 3) == 5.0

def test_div_by_zero():
    with pytest.raises(ValueError):
        assert divide(10, 0)