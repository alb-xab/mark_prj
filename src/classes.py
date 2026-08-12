class Product:

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        return self.price * self.quantity + other.price * other.quantity


    @classmethod
    def new_product(cls, product: dict, products_list: list):
        if products_list is None:
            products_list = []

        for existing_product in products_list:
            if existing_product.name == product["name"]:
                existing_product.quantity += product["quantity"]
                if product["price"] > existing_product.price:
                    existing_product.price = product["price"]
                return existing_product

        return cls(
            product["name"],
            product["description"],
            product["price"],
            product["quantity"],
        )

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return

        if price < self.__price:
            confirmation = input("Подтвердите понижение цены: y или n?")
            if confirmation.lower() != "y":
                print("Вы отменили изменение цены")
                return

        self.__price = price


class Category:
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def __str__(self):
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f'{self.name}, количество продуктов: {total_quantity} шт.'


    def add_product(self, product):
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        result = ""
        for product in self.__products:
            result += f"{str(product)}\n"
        return result

    def get_product_list(self):
        return self.__products