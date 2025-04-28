import pytest
from main import *

def test_method_one():
    result = method_one([1, 2, 1, 2, 2])
    assert result == [2, 2]

def test_method_one_raise():
    with pytest.raises(ValueError) as exc_info:
        method_one([2, 2, 2, 2])
    assert exc_info.type is ValueError


@pytest.mark.parametrize("data_all, expected",[
    ([2, 2, 2, 2], False),
    ([1, 2, 3], False),
    ([1, 2, 1], True)
])
def test_method_two(data_all, expected):
    assert method_two(data_all) == expected

@pytest.mark.parametrize("data_fail", [
    [2, 2, 2, 2],
    [1, 2, 3]
])
def test_method_two_fail(data_fail):
    assert not method_two(data_fail)