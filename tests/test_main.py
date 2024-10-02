import pytest
from typing import Any
from src.main import Product, Category


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
    category2 = Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         [product4])
    return category2


def test_category_init(category):
    assert category.name == "Телевизоры"
    assert category.description == "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником"


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
