from src.product.product import Product


class Smartphone(Product):
    perfomance: str
    model: str
    RAM: str
    color: str

    def __init__(self,
                 name: str, description: str, price: float, quantity: int,
                 perfomance: str, model: str, RAM: str, color: str
                 ):
        """
        Смартфон
        :param name: имя
        :param description: описание
        :param price: цена
        :param quantity: количество
        :param perfomance: проивзодительность
        :param model: модель
        :param RAM: ОЗУ
        :param color: цвет
        """
        super().__init__(name, description, price, quantity)
        self.perfomance = perfomance
        self.model = model
        self.RAM = RAM
        self.color = color

