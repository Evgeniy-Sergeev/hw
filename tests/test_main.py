import pytest
from src.main import Product, Smartphone, LawnGrass, Category


def test_product_initialization():
    """Тест корректной инициализации класса Product"""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_price_setter():
    """Тест установки новой цены"""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product.price = 200000.0
    assert product.price == 200000.0

    product.price = -5000
    assert product.price == 200000.0


def test_product_str_method():
    """Тест метода __str__ для класса Product"""
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert str(product) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_addition():
    """Тест сложения двух продуктов одного типа"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    total_value = product1 + product2
    assert total_value == (180000.0 * 5 + 210000.0 * 8)


def test_product_add_type_error():
    """Тест исключения TypeError при сложении разных типов продуктов"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    lawn_grass = LawnGrass("Газон", "Для сада", 500.0, 30, "Россия", 7, "Зеленый")

    with pytest.raises(TypeError):
        product1 + lawn_grass


def test_smartphone_initialization():
    """Тест корректной инициализации класса Smartphone"""
    smartphone = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, "A16 Bionic", "iPhone 15", 512, "Gray")
    assert smartphone.name == "Iphone 15"
    assert smartphone.description == "512GB, Gray space"
    assert smartphone.price == 210000.0
    assert smartphone.quantity == 8
    assert smartphone.efficiency == "A16 Bionic"
    assert smartphone.model == "iPhone 15"
    assert smartphone.memory == 512
    assert smartphone.color == "Gray"


def test_lawn_grass_initialization():
    """Тест корректной инициализации класса LawnGrass"""
    lawn_grass = LawnGrass("Газон", "Для сада", 500.0, 30, "Россия", 7, "Зеленый")
    assert lawn_grass.name == "Газон"
    assert lawn_grass.description == "Для сада"
    assert lawn_grass.price == 500.0
    assert lawn_grass.quantity == 30
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == 7
    assert lawn_grass.color == "Зеленый"


def test_category_initialization():
    """Тест корректной инициализации категории"""
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны", "Описание смартфонов", [product1, product2])

    assert category.name == "Смартфоны"
    assert category.description == "Описание смартфонов"
    assert len(category.products.splitlines()) == 2  # Два продукта в категории


def test_category_add_product():
    """Тест добавления продукта в категорию"""
    category = Category("Смартфоны", "Описание смартфонов")
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    category.add_product(product)
    assert len(category.products.splitlines()) == 1
    assert "Samsung Galaxy S23 Ultra" in category.products
