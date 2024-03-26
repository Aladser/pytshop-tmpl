import pytest
from classes import Category, Product

title = 'еда'
description = 'здесь должна быть реклама'
# товары для теста категории
prd1 = Product('Хлеб', 5)
prd2 = Product('Хлеб', 7)
prd3 = Product('Чай', 15)
prd4 = Product('Сахар', 20)
products = [prd1, prd2, prd3, prd4]


@pytest.fixture
def category():
    return Category(title, products, description)


def test_count_categories(category):
    assert category.count == 1


def test_init(category):
    assert category.title == title
    assert category.products == products
    assert category.description == description


def test_products(category):
    assert category.products_count() == 3
