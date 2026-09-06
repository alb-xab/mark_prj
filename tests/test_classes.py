import pytest

from src.classes import Category, LawnGrass, Order, Product, Smartphone
from src.ExceptionsClass import ZeroQuantityError


def test_product_init(sample_product):
    """Проверка корректной инициализации Product."""
    assert sample_product.name == "Test Product"
    assert sample_product.description == "Test description"
    assert sample_product.price == 100.0
    assert sample_product.quantity == 10


def test_product_another():
    """Дополнительная проверка с другими значениями."""
    p = Product("A", "B", 1.5, 3)
    assert p.name == "A"
    assert p.price == 1.5
    assert p.quantity == 3


def test_add_product(sample_category):
    new_product = Product("New Item", "desc", 50.0, 3)
    sample_category.add_product(new_product)
    assert "New Item, 50.0 руб. Остаток: 3 шт." in sample_category.products


def test_products_property_format(sample_product):
    category = Category("Cat", "desc", [sample_product])
    assert category.products == ("Test Product, 100.0 руб. Остаток: 10 шт.\n")


def test_new_product_creates():
    data = {
        "name": "Phone",
        "description": "desc",
        "price": 1000.0,
        "quantity": 5,
    }
    product = Product.new_product(data, [])
    assert product.name == "Phone"
    assert product.price == 1000.0
    assert product.quantity == 5


def test_new_product_duplicate_merges():
    existing = Product("Phone", "old desc", 1000.0, 5)
    data = {
        "name": "Phone",
        "description": "new desc",
        "price": 1500.0,
        "quantity": 3,
    }

    result = Product.new_product(data, [existing])

    assert result is existing
    assert result.quantity == 8
    assert result.price == 1500.0


def test_product_str(sample_product):
    assert str(sample_product) == "Test Product, 100.0 руб. Остаток: 10 шт."


def test_product_add():
    a = Product("A", "", 100.0, 10)
    b = Product("B", "", 200.0, 2)
    assert a + b == 1400


def test_price_getter(sample_product):
    assert sample_product.price == 100.0


def test_price_setter_increase(sample_product):
    sample_product.price = 200.0
    assert sample_product.price == 200.0


def test_price_setter_zero_or_negative(sample_product, capsys):
    sample_product.price = 0
    assert sample_product.price == 100.0

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out

    sample_product.price = -10
    assert sample_product.price == 100.0


def test_price_decrease_confirm_yes(sample_product, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "y")
    sample_product.price = 50.0
    assert sample_product.price == 50.0


def test_price_decrease_confirm_no(sample_product, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")
    sample_product.price = 50.0
    assert sample_product.price == 100.0


def test_smartphone_init():
    phone = Smartphone("Iphone 15", "512GB", 210000.0, 8, 98.2, "15", 512, "Gray space")
    assert phone.name == "Iphone 15"
    assert phone.price == 210000.0
    assert phone.quantity == 8
    assert phone.efficiency == 98.2
    assert phone.model == "15"
    assert phone.memory == 512
    assert phone.color == "Gray space"
    assert isinstance(phone, Product)


def test_lawn_grass_init():
    grass = LawnGrass(
        "Газонная трава", "Элитная", 500.0, 20, "Россия", "7 дней", "Зеленый"
    )
    assert grass.name == "Газонная трава"
    assert grass.country == "Россия"
    assert grass.germination_period == "7 дней"
    assert grass.color == "Зеленый"
    assert isinstance(grass, Product)


def test_add_same_smartphones():
    s1 = Smartphone("A", "", 100.0, 10, 90.0, "A", 128, "black")
    s2 = Smartphone("B", "", 200.0, 2, 91.0, "B", 256, "white")
    assert s1 + s2 == 1400


def test_add_same_lawn_grass():
    g1 = LawnGrass("A", "", 500.0, 20, "RU", "7 дней", "green")
    g2 = LawnGrass("B", "", 450.0, 15, "US", "5 дней", "dark")
    assert g1 + g2 == 500.0 * 20 + 450.0 * 15


def test_add_different_classes_raises():
    phone = Smartphone("A", "", 100.0, 1, 90.0, "A", 128, "black")
    grass = LawnGrass("B", "", 500.0, 1, "RU", "7 дней", "green")
    with pytest.raises(TypeError):
        phone + grass


def test_add_smartphone_to_category(sample_category):
    phone = Smartphone("A", "", 100.0, 1, 90.0, "A", 128, "black")
    sample_category.add_product(phone)
    assert "A, 100.0 руб. Остаток: 1 шт." in sample_category.products


def test_add_lawn_grass_to_category(sample_category):
    grass = LawnGrass("Grass", "", 500.0, 2, "RU", "7 дней", "green")
    sample_category.add_product(grass)
    assert "Grass, 500.0 руб. Остаток: 2 шт." in sample_category.products


def test_add_non_product_raises(sample_category):
    with pytest.raises(TypeError):
        sample_category.add_product("Not a product")


def test_product_init_zero_quantity():
    with pytest.raises(
        ValueError, match="Товар с нулевым количеством не может быть добавлен"
    ):
        Product("Телефон", "Описание", 50000, 0)


#         Тесты категорий


def test_category_init(sample_category, sample_product):
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Category description"
    assert sample_category.products == ("Test Product, 100.0 руб. Остаток: 10 шт.\n")


def test_category_init_empty_products():
    cat = Category("Empty", "No products", [])
    assert cat.name == "Empty"
    assert cat.products == ""


def test_product_count_increment(sample_category, sample_product):
    assert Category.product_count == 1

    p1 = Product("p1", "", 1, 1)
    p2 = Product("p2", "", 1, 1)
    p3 = Product("p3", "", 1, 1)
    Category("Many", "", [p1, p2, p3])
    assert Category.product_count == 4


def test_category_str(sample_category):
    # у sample_product quantity=10
    assert str(sample_category) == "Test Category, количество продуктов: 10 шт."


def test_category_str_total_quantity():
    p1 = Product("A", "", 100.0, 5)
    p2 = Product("B", "", 200.0, 8)
    cat = Category("Phones", "", [p1, p2])
    assert str(cat) == "Phones, количество продуктов: 13 шт."


def test_category_average_price_with_products():
    p1 = Product("Товар1", "Описание1", 100, 2)
    p2 = Product("Товар2", "Описание2", 200, 3)
    category = Category("Электроника", "Техника", [p1, p2])
    assert category.middle_price() == 150.0  # (100+200)/2


def test_category_average_price_empty():
    empty_category = Category("Пустая", "Без товаров", [])
    assert empty_category.middle_price() == 0


def test_category_add_product_zero_quantity():
    product = Product(
        "Книга", "Интересная", 300, 1
    )  # создаём с положительным количеством
    product.quantity = 0  # имитируем, что остаток стал нулевым
    category = Category("Книги", "Разные", [])

    with pytest.raises(
        ZeroQuantityError,
        match="Товар с нулевым количеством не может быть добавлен в категорию",
    ):
        category.add_product(product)


# Тесты для Order


def test_order_init(sample_product):
    order = Order(sample_product, 3)
    assert order.product is sample_product
    assert order.quantity == 3
    assert order.total_price == 300.0


def test_order_str(sample_product):
    order = Order(sample_product, 2)
    text = str(order)
    assert "Test Product" in text
    assert "2" in text
    assert "200.0" in text


def test_order_with_smartphone():
    phone = Smartphone("A", "desc", 100.0, 5, 90.0, "A", 128, "black")
    order = Order(phone, 2)
    assert order.total_price == 200.0


def test_order_init_zero_quantity():
    "Тест нулевого количество Заказа"
    product = Product("Часы", "Наручные", 5000, 2)
    with pytest.raises(
        ZeroQuantityError,
        match="Товар с нулевым количеством не может быть добавлен в категорию",
    ):
        Order(product, 0)
