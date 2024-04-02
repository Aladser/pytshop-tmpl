import pytest
from classes import Category, Product


@pytest.fixture
def name():
    return 'еда'


@pytest.fixture
def description():
    return 'здесь должна быть реклама'


@pytest.fixture
def products():
    return [
        Product(name='Хлеб', price=5, quantity=1, description='Товар 1')
    ]


@pytest.fixture
def category(name, products, description):
    return Category(name, products, description)


def test_init(category, name, products, description):
    assert category.name == name
    assert category.description == description
    assert category.products == [str(prd) for prd in products]
    assert Category.products_count == 1
    assert Category.count == 1
    assert len(category) == 1


def test_work(category):
    print()
    print(category.products)
    # добавление товара
    prd = Product(name='Хлеб', price=5, quantity=1, description='Товар 1')
    category.add_product(prd)
    assert Category.products_count == 2
    # дубль товара
    prd = Product(name='Хлеб1', price=5, quantity=1, description='Товар 1')
    category.add_product(prd)
    assert Category.products_count == 3