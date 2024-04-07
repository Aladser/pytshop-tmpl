from src.product import Product


class Smartphone(Product):
    perfomance: str
    model: str
    RAM: str
    color: str

    def __init__(self,
                 name: str, price: float, quantity: int, description: str,
                 perfomance: str, model: str, RAM: str, color: str
                 ):
        """
        Смартфон
        :param name: имя
        :param price: цена
        :param quantity: количество
        :param description: описание
        :param perfomance: проивзодительность
        :param model: модель
        :param RAM: ОЗУ
        :param color: цвет
        """
        super().__init__(name, price, quantity, description)
        self.perfomance = perfomance
        self.model = model
        self.RAM = RAM
        self.color = color

