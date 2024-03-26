import pytest
from classes import Product


@pytest.fixture
def product():
    return Product('Хлеб', 11.11, 5)


def test_init(product):
    assert product.title == 'Хлеб'
    assert product.price == 11.11
    assert product.count == 5
