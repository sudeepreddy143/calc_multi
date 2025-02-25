import pytest
from commands.basic import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 5), (-1, 5, 4), (10, -10, 0)
])
def test_add(a, b, expected):
    assert AddCommand().execute(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 5, 5), (0, 5, -5), (-5, -5, 0)
])
def test_subtract(a, b, expected):
    assert SubtractCommand().execute(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (3, 3, 9), (5, 0, 0), (-2, -3, 6)
])
def test_multiply(a, b, expected):
    assert MultiplyCommand().execute(a, b) == expected

@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5), (-10, -2, 5), (5, 2, 2.5)
])
def test_divide(a, b, expected):
    assert DivideCommand().execute(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError):
        DivideCommand().execute(5, 0)
