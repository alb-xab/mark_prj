from src.classes import Category, Product


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
