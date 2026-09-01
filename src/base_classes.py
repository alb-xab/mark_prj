from abc import ABC, abstractmethod


class BaseProduct(ABC):

    def __str__(self):
        pass

    def __add__(self, other):
        pass

    def price(self):
        pass

    @classmethod
    @abstractmethod
    def new_product(cls, product: dict, products_list: list):
        pass


class BaseDate(ABC):

    def __str__(self):
        pass


class MixinLog:

    def __init__(self):
        print(repr(self))

    def __repr__(self):
        return f"{self.__class__.__name__} ('{self.name}', '{self.description}', {self.price}, {self.quantity})"
