class LogMixin:
    """ Вывод информации в консоль о том, что был создан объект"""
    def get_props(self) -> str:
        """ Класс ([атрибуты])"""
        param_values = ""
        for key, value in self.__dict__.items():
            param_values += f"{key}:{value}, "
        if len(self.__dict__.values()) > 0:
            param_values = param_values[:-2]
        return f"{self.__class__.__name__}({param_values})"

    def log(self):
        print(self.get_props())
