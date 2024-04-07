from src.product import Product


class Grass(Product):
    country_manufacturer: str
    germination_period: int
    color: str

    def __init__(self,
                 name: str, price: float, quantity: int, description: str,
                 country_manufacturer: str, germination_period: int, color: str
                 ):
        """
        Трава
        :param name: имя
        :param price: цена
        :param quantity: количество
        :param description: описание
        :param country_manufacturer: страна-производитель
        :param germination_period: срок прорастания
        :param color: цвет
        """
        super().__init__(name, price, quantity, description)
        self.country_manufacturer = country_manufacturer
        self.germination_period = germination_period
        self.color = color
