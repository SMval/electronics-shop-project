"""Здесь надо написать тесты с использованием pytest для модуля item."""
from src.item import Item
import pytest


item1 = Item("Смартфон", 10000, 20)

# Testcase 1
assert item1.name == "Смартфон"
assert item1.price == 10000
assert item1.quantity == 20

item2 = Item("Ноутбук", 20000, 5)

# Testcase 2
assert item2.name == "Ноутбук"
assert item2.price == 20000
assert item2.quantity == 5

item1.calculate_total_price()
# Testcase 3
assert item1.calculate_total_price() == 200000

item2.calculate_total_price()
# Testcase 4
assert item2.calculate_total_price() == 100000

item1.apply_discount()
# Testcase 5
assert item1.price == 10000

item2.apply_discount()
# Testcase 6
assert item2.price == 20000

Item.pay_rate = 0.8
item1.apply_discount()
# Testcase 7
assert item1.price == 8000.0
