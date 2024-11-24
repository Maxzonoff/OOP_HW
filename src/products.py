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
        if quantity > 0:
            self.quantity = quantity
        else:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
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

    def middle_price(self):
        try:
            total_price = 0
            for prod in self.__products:
                total_price += prod.price
            return round(total_price / len(self.__products), 2)
        except ZeroDivisionError:
            return 0


if __name__ == "__main__":
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print(
            "Возникла ошибка ValueError прерывающая работу программы при попытке добавить продукт с нулевым количеством"
        )
    else:
        print(
            "Не возникла ошибка ValueError при попытке добавить продукт с нулевым количеством"
        )

    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    category1 = Category(
        "Смартфоны", "Категория смартфонов", [product1, product2, product3]
    )

    print(category1.middle_price())

    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(category_empty.middle_price())
