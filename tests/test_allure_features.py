import time
import pytest


@pytest.mark.xfail()
def test_xfail():
    assert False


@pytest.mark.xfail()
def test_xpass():
    assert False


# def test_unexpected_fail():
#     assert False


# @pytest.mark.parametrize('param1', [0, 1, 2])
# @pytest.mark.parametrize('param2', ['a', 'b', 'c'])
# def test_parametrized(param1, param2):
#     assert param1
#     assert param2


@pytest.mark.skip()
def test_skip():
    assert True


def test_long_test():
    time.sleep(3)
    assert True
