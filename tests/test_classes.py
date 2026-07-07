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


def test_category_init(sample_category, sample_product):
    assert sample_category.name == "Test Category"
    assert sample_category.description == "Category description"
    assert sample_category.products == [sample_product]


def test_category_init_empty_products():
    cat = Category("Empty", "No products", [])
    assert cat.name == "Empty"
    assert cat.products == []


def test_product_count_increment(sample_category, sample_product):
    assert Category.product_count == 1

    p1 = Product("p1", "", 1, 1)
    p2 = Product("p2", "", 1, 1)
    p3 = Product("p3", "", 1, 1)
    Category("Many", "", [p1, p2, p3])
    assert Category.product_count == 4
