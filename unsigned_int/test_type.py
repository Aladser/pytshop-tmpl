import pytest
from unsigned_int.unsigned_int import UnsignedInt


def test_work():
    val = UnsignedInt(6)
    # проверка операции
    assert val + 4 == 10
    assert val - 1 == 5
    assert val * 5 == 30
    assert val / 4 == 1
    assert val % 4 == 2
    assert val ** 2 == 36
    # проверка отрицательных чисел
    assert val + -4 == 2
    assert val - -1 == 7
    assert val * -5 == -30
    assert val / -3 == -2
    assert val % -4 == -2
    val = 5
    assert val ** -2 == 0.04