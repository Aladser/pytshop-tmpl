from classes import Smartphone


def test_init():
    params = {
        'name': 'Xiaomi',
        'description': 'смартфон выполнен в корпусе серого цвета и предлагает мощные характеристики для комфортного решения разных задач',
        'price': 40000,
        'quantity': 3,
        'perfomance': 687373,
        'model': '12X',
        'RAM': '32 Гб',
        'color': 'зеленый'
    }
    smartphone = Smartphone(**params)
    assert smartphone.perfomance == params['perfomance']
    assert smartphone.model == params['model']
    assert smartphone.RAM == params['RAM']
    assert smartphone.color == params['color']