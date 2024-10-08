import pytest
from typing import Any
from src.main import Product, Category, Smartphone, LawnGrass


@pytest.fixture
def product() -> Any:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    return product1


def test_product_init(product) -> Any:
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


@pytest.fixture()
def category() -> Any:
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4]
    )
    return category2


def test_category_init(category):
    assert category.name == "Телевизоры"
    assert category.description == (
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"
    )


def test_product_creation():
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_price_setter_positive():
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product.price = 150000.0
    assert product.price == 150000.0


def test_price_setter_negative():
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product.price = -5000.0
    assert product.price == 210000.0


def test_price_setter_zero():
    product = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product.price = 0
    assert product.price == 210000.0


def test_new_product():
    product_data = {
        "name": "Samsung Galaxy S23 Ultra",
        "description": "256GB, Серый цвет, 200MP камера",
        "price": 180000.0,
        "quantity": 5
    }
    new_product = Product.new_product(product_data)
    assert new_product.name == "Samsung Galaxy S23 Ultra"
    assert new_product.description == "256GB, Серый цвет, 200MP камера"
    assert new_product.price == 180000.0
    assert new_product.quantity == 5


def test_category_creation():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    category = Category("Смартфоны", "Описание категории", [product1, product2])
    assert category.products == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
        "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


def test_product_add():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    expected_sum = (180000.0 * 5) + (210000.0 * 8)
    assert product1 + product2 == expected_sum


def test_smartphone_init():
    smartphone = Smartphone("Iphone 15", "512GB, Gray space", 210000.0, 8, "A16 Bionic", "Iphone", 512, "Gray")
    assert smartphone.name == "Iphone 15"
    assert smartphone.memory == 512
    assert smartphone.color == "Gray"


def test_lawngrass_init():
    grass = LawnGrass("Газонная трава", "Для футбольных полей", 1500.0, 100, "Россия", 7, "Зеленый")
    assert grass.name == "Газонная трава"
    assert grass.country == "Россия"
    assert grass.germination_period == 7


def test_product_add_same_type():
    smartphone1 = Smartphone("Iphone 15", "512GB", 210000.0, 8, "A16 Bionic", "Iphone", 512, "Gray")
    smartphone2 = Smartphone("Samsung Galaxy", "256GB", 180000.0, 5, "Exynos", "Galaxy", 256, "Black")
    assert smartphone1 + smartphone2 == (210000.0 * 8 + 180000.0 * 5)


def test_product_add_different_type():
    smartphone = Smartphone("Iphone 15", "512GB", 210000.0, 8, "A16 Bionic", "Iphone", 512, "Gray")
    grass = LawnGrass("Газонная трава", "Для футбольных полей", 1500.0, 100, "Россия", 7, "Зеленый")
    with pytest.raises(TypeError):
        smartphone + grass


def test_add_valid_product_to_category():
    smartphone = Smartphone("Iphone 15", "512GB", 210000.0, 8, "A16 Bionic", "Iphone", 512, "Gray")
    category = Category("Смартфоны", "Категория смартфонов")
    category.add_product(smartphone)
    assert smartphone in category._products


def test_add_invalid_product_to_category():
    non_product = "Это не продукт"
    category = Category("Смартфоны", "Категория смартфонов")
    with pytest.raises(TypeError):
        category.add_product(non_product)
