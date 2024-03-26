import pytest
from classes import Category


@pytest.fixture
def category():
    return Category('Еда', ['Хлеб', 'Хлеб', 'Чай', 'Сахар'])


def test_count_categories(category):
    assert category.count == 1


def test_init(category):
    assert category.title == 'Еда'
    assert category.products == {'Хлеб', 'Чай', 'Сахар'}
    assert category.description == ""


def test_products(category):
    assert category.products_count() == 3
