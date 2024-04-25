import pytest
from src import Category, CategoryProductRange
from src.product import Product


@pytest.fixture()
def products():
    return [
        Product(name='Хлеб 1', price=5, quantity=1, description='Товар 1'),
        Product(name='Хлеб 2', price=10, quantity=2, description='Товар 2'),
        Product(name='Хлеб 3', price=15, quantity=3, description='Товар 3')
    ]


def test_iterator(products):
    products_str = [*products]
    ctg = Category('aaaa', "", products)
    cp_iterator = CategoryProductRange(ctg)
    print()
    for i in cp_iterator:
        print(ctg.products[i])
        assert ctg.products[i] == str(products_str[i])
