import pytest
from classes import Category


@pytest.fixture
def category():
    return Category('Продукты', ['Хлеб', 'Хлеб', 'Молоко', 'Сахар'])


def test_category_count(category):
    assert category.count == 1


def test_init(category):
    assert category.title == 'Продукты'
    assert category.products == set(['Хлеб', 'Молоко', 'Сахар'])


def test_products_count(category):
    assert category.products_count() == 3
