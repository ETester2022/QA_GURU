"""
Протестируйте классы из модуля homework/models_hw8.py
"""
import pytest

from models_hw8 import Product


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(33) is True

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(999) == "Товар оплачен"

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError, match="Продуктов не хватает."):
            product.buy(product.quantity + 1)
