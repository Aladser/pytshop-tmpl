class LogMixin:
    def get_props_str(self) -> str:
        return f"{self.__class__.__name__}({param_values})"

    def get_props_dict(self) -> dict:
        props_dict = {}
        return props_dict

        print(self.get_props_str())
