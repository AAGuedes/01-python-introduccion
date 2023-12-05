"""
Contenedores
"""


class Product:
    "Product class"

    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"Product: {self.name} - Price: {self.price}"


class Category:
    "Category class"

    products = []

    def __init__(self, name, products):
        self.name = name
        self.products = products

    def add(self, product):
        "Add a new product"
        self.products.append(product)

    def print(self):
        "Print all products"
        for product in self.products:
            print(product)


kayak = Product("Kayak", 1000)
surfboard = Product("Surfboard", 750)
bicycle = Product("Bicycle", 500)

sports = Category("Sports", [kayak, surfboard])
sports.add(bicycle)
sports.print()
