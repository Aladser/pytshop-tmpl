import pytest
from classes import Product


@pytest.fixture
def product():
    return Product('Хлеб', 1.1, 5)


def test_init(product):
    assert product.title == 'Хлеб'
    assert product.price == 1.1
    assert product.count == 5
    assert product.description == ""
