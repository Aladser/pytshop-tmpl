# Шаблон интернет-магазина

+ ``classes``
    * ``product``
      + ``Product``
      + ``Grass``
      + ``Smartphone``
    * ``category``
      + ``Category``
      + ``CategoryProductRange``
+ ``tests``
    * ``product``
      + ``test_product``
      + ``test_grass``
      + ``test_smartphone``
    * ``category``
      + ``test_category``
      + `test_ctgprd_iterator`
+ ``load_data.py`` - парсинг JSON файла и выгрузка категорий и товаров из него.
