from classes.category import Category


class CategoryProductRange:
    def __init__(self, category: Category):
        self.stop = category.products_count

    def __iter__(self):
        self.current_value = -1
        return self

    def __next__(self):
        if self.current_value + 1 < self.stop:
            self.current_value += 1
            return self.current_value
        else:
            raise StopIteration
