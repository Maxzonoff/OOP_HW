from abc import ABC
from typing import Any


class BaseProduct(ABC):
    name: str
    description: str
    price: float
    quantity: int


class MixinLog:
    def __init__(self, *args, **kwargs):
        print(repr(self))


class Product(BaseProduct, MixinLog):

    def __init__(
            self, name: str, description: str, price: float, quantity: int
    ) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity})"

    @classmethod
    def new_product(cls, params: dict) -> "Product":
        return cls(
            params["name"],
            params["description"],
            params["price"],
            params["quantity"],
        )

    def __add__(self, other):
        if type(self) is not type(other):
            raise TypeError
        return self.__price * self.quantity + other.__price * other.quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price


class Smartphone(Product):
    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            efficiency: float,
            model: str,
            memory: int,
            color: str,
    ) -> None:
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity}, "
            f"{self.efficiency}, {self.model}, {self.memory}, {self.color})"
        )


class LawnGrass(Product):
    def __init__(
            self,
            name: str,
            description: str,
            price: float,
            quantity: int,
            country: str,
            germination_period: str,
            color: str,
    ) -> None:
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)

    def __repr__(self):
        return (
            f"{self.__class__.__name__}({self.name}, {self.description}, {self.price}, {self.quantity}, "
            f"{self.country}, {self.germination_period}, {self.color})"
        )


class Category:
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)
        self.total_products_quantity = 0

    def __str__(self):
        for product in self.__products:
            self.total_products_quantity += product.quantity
        return f"{self.name}, количество продуктов: {self.total_products_quantity} шт."

    def add_product(self, product: Any) -> None:
        if not isinstance(product, Product):
            raise TypeError
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        prod_str = []
        for prod in self.__products:
            prod_str.append(str(prod))
        return " ".join(prod_str)


if __name__ == '__main__':
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [product1, product2, product3])

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)
