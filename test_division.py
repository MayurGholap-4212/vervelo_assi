import pytest
from division import divide

def test_divide_valid():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3

def test_divide_zero():
    with pytest.raises(ValueError):
        divide(5, 0)
