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
    product.price =  price
    assert product.price ==  price
    # нулевая цена
    product.price = 0
    assert product.price ==  price


def test_create():
    title = 'яблоко'
    price = 11.5
    count = 3
    product = Product.create({'title': title, 'price': price, 'count': count})
    assert product.title ==  title
    assert product.price == price
    assert product.count == count
