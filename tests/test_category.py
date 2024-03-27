import pytest
from classes import Category, Product


@pytest.fixture
def title():
    return 'еда'


@pytest.fixture
def description():
    return 'здесь должна быть реклама'


@pytest.fixture
def products():
    return [
        Product('Хлеб', 5, 1, 'Товар 1'),
        Product('Чай', 15, 3, 'Товар 2'),
        Product('Сахар', 20, 4, 'Товар 3')
    ]


@pytest.fixture
def category(title, products, description):
    return Category(title, products, description)


def test_products(category):
    assert Category.products_count == 3


def test_count_categories(category):
    # в таком случае неизбежно создается 2 экземпляра
    assert Category.count == 2


def test_init(category, title, products, description):
    assert category.title == title
    assert category.description == description
    assert category.products == products
