import pytest
from repl import parse_expression

@pytest.mark.parametrize("expression, expected", [
    ("6+5", ("+", 6.0, 5.0)),
    ("10 - 3", ("-", 10.0, 3.0)),
    ("4.5 * 2", ("*", 4.5, 2.0)),
    ("12 / 4", ("/", 12.0, 4.0))
])
def test_parse_expression(expression, expected):
    assert parse_expression(expression) == expected

def test_parse_invalid_expression():
    assert parse_expression("invalid") is None
