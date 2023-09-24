"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item

item1 = Item("Смартфон", 10000, 20)
item2 = Item("Ноутбук", 20000, 5)


# Testcase 1 Тест на создание экземпляра
def test___init__():
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20
    assert item2.name == "Ноутбук"
    assert item2.price == 20000
    assert item2.quantity == 5


# Testcase 2 Тест на подсчет общей стоимости
def test_calculate_total_price():
    assert item1.calculate_total_price() == 200000
    assert item2.calculate_total_price() == 100000


# Testcase 3 Тест на подсчет стоимости со скидкой
def test_apply_discount():
    assert item1.price == 10000
    assert item2.price == 20000
