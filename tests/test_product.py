import pytest
from classes import Product


@pytest.fixture
def product():
    return Product(title='Хлеб', price=1.1, count=5, description="товар")


def test_init(product):
    assert product.title == 'Хлеб'
    assert product.price == 1.1
    assert product.count == 5
    assert product.description == "товар"
