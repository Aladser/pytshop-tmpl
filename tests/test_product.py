import pytest
from classes import Product


@pytest.fixture
def product():
    return Product(title='Хлеб', price=10, count=5, description="товар")


def test_init(product):
    assert product.title == 'Хлеб'
    assert product.price == 10
    assert product.count == 5
    assert product.description == "товар"


def test_add_plus(product):
    product.price = 15
    assert product.price == 15