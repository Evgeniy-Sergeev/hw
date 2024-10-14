import pytest
from src.main import Product, Category


def test_product_zero_quantity():
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Товар с нулевым количеством", "Описание", 1000.0, 0)


def test_middle_price():
    product1 = Product("Продукт 1", "Описание 1", 100.0, 5)
    product2 = Product("Продукт 2", "Описание 2", 200.0, 3)
    category = Category("Категория", "Описание", [product1, product2])

    assert category.middle_price() == 150.0


def test_empty_category():
    category = Category("Пустая категория", "Описание", [])
    assert category.middle_price() == 0
