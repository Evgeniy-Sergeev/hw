class Product:
    def __init__(self, name, description, price, quantity):
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category:
    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.products = products if products is not None else []

    def middle_price(self):
        if not self.products:
            return 0
        total_price = sum(product.price for product in self.products)
        return total_price / len(self.products)


if __name__ == '__main__':
    try:
        product_invalid = Product("Бракованный товар", "Неверное количество", 1000.0, 0)
    except ValueError as e:
        print("Возникла ошибка:", e)
    else:
        print("Продукт создан успешно")

    # Создание нескольких товаров
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Создание категории с товарами
    category1 = Category("Смартфоны", "Категория смартфонов", [product1, product2, product3])
    print(f"Средняя цена в категории: {category1.middle_price()} руб.")

    # Создание пустой категории
    category_empty = Category("Пустая категория", "Категория без продуктов", [])
    print(f"Средняя цена в пустой категории: {category_empty.middle_price()} руб.")
