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


def test_price(product):
    price = 15
    # установка новой цены
    product.price = price
    assert product.price == price
    # нулевая цена
    with pytest.raises(Exception):
        product.price = 0


def test_create():
    title = 'яблоко'
    price = 11.5
    count = 3
    description = 'aaaaaaaaaaaaaaaa'
    product = Product.create({'title': title, 'price': price, 'count': count, 'description': description})
    assert product.title == title
    assert product.price == price
    assert product.count == count
    assert product.description == description
