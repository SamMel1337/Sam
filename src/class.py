class Product:
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    total_categories = 0
    total_products = 0

    name: str
    description: str
    products: str

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.products = []

        Category.total_categories += 1


def add_product(self, product):
    if isinstance(product, Product):
        self.products.append(product)
        # Увеличиваем общее количество товаров при добавлении нового продукта
        Category.total_products += 1
    else:
        raise ValueError("Only instances of Product can be added.")


def __str__(self):
    return f"Category(name={self.name}, description={self.description}, " f"total products={len(self.products)})"


if __name__ == "__main__":
    # Создаем продукты
    product1 = Product("Laptop", "A high-performance laptop", 1200.99, 10)
    product2 = Product("Smartphone", "A latest model smartphone", 799.99, 25)

    # Создаем категорию
    electronics_category = Category("Electronics", "Devices and gadgets")
