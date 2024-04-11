# Шаблон интернет-магазина

+ *general*
    * ``MixingLog`` - вывод информации о созданном объекте
    * ``StrImpl`` - абстрактный класс метода ``__str__``
+ *classes*
    * ``Category``
    * ``CategoryProductRange``
    * ``Order``
    * *product*
      + ``BaseProduct`` - абстрактный класс продукта
      + ``Product``
      + ``Grass``
      + ``Smartphone``
+ *tests*
+ *load_data.py* - парсинг JSON файла и выгрузка категорий и товаров из него.
