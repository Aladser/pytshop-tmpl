import pytest
from src import Grass


def test_init():
    params = {
        'name': 'газонная',
        'price': 10,
        'quantity': 5,
        'description': 'городская',
        'country_manufacturer': 'Россия',
        'germination_period': '1 year',
        'color': 'зеленый'
    }
    grass = Grass(**params)
    assert grass.country_manufacturer == params['country_manufacturer']
    assert grass.germination_period == params['germination_period']
    assert grass.color == params['color']
