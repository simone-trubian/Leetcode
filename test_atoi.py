import pytest
from atoi import myAtoi

def test_myatoi():
    assert myAtoi("42") == 42
    assert myAtoi("  42") == 42
    assert myAtoi("-42") == -42
    assert myAtoi("    -42") == -42

    assert myAtoi("") == 0
    assert myAtoi("hello 42") == 0
    assert myAtoi("-hello 42") == 0
    assert myAtoi("-0042") == -42
    assert myAtoi("  -0012a42") == -12
