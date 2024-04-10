class MixinConsoleLog:
    def __init__(self):
        self.log()

    def log(self):
        param_values = ""
        for value in self.__dict__.values():
            param_values += f"'{value}', " if isinstance(value, str) else f"{value}, "
        if len(self.__dict__.values()) > 0:
            param_values = param_values[:-2]
        print(f"{self.__class__.__name__}({param_values})")