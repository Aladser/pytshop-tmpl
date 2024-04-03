import pytest
from src import Product


@pytest.fixture
def product():
    return Product(name='Хлеб', price=10, quantity=5, description="товар")


def test_init(product):
    assert product.name == 'Хлеб'
    assert product.price == 10
    assert product.quantity == 5
    assert len(product) == 5
    with pytest.raises(Exception):
        assert product.quantity == -5
    assert product.description == "товар"
    print(f"\n{product}", end='')


def test_price(product):
    price = 15
    # установка новой цены
    product.price = price
    assert product.price == price
    # нулевая цена
    with pytest.raises(Exception):
        product.price = 0


def test_create(product):
    title = 'яблоко'
    price = 11.5
    count = 3
    description = 'фрукт'
    product = Product.create({'name': title, 'price': price, 'quantity': count, 'description': description})
    assert product.name == title
    assert product.price == price
    assert product.quantity == count
    assert product.description == description


def test_add():
    prd = Product(name='Хлеб 1', price=5, quantity=5, description="товар 1")
    other = Product(name='Хлеб 2', price=25, quantity=3, description="товар 2")
    assert prd + other == 100
