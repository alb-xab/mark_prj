from abc import ABC

import pytest

from src.base_classes import BaseDate, BaseProduct, MixinLog
from src.classes import Category, Order, Product, Smartphone


def test_base_product_is_abstract():
    with pytest.raises(TypeError):
        BaseProduct()


def test_product_inherits_base_product():
    assert issubclass(Product, BaseProduct)
    assert issubclass(Smartphone, BaseProduct)


def test_mixin_log_prints_on_create(capsys):
    Product("Продукт1", "Описание продукта", 1200, 10)
    captured = capsys.readouterr()
    assert "Product" in captured.out
    assert "Продукт1" in captured.out
    assert "1200" in captured.out
    assert "10" in captured.out


def test_product_inherits_mixin():
    assert issubclass(Product, MixinLog)


def test_category_and_order_inherit_base_date():
    assert issubclass(Category, BaseDate)
    assert issubclass(Order, BaseDate)


def test_base_date_is_abc():
    assert issubclass(BaseDate, ABC)
