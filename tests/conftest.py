import pytest

from classes import Category, Product


@pytest.fixture
def sample_product():
    return Product(
        name="Test Product", description="Test description", price=100.0, quantity=10
    )


@pytest.fixture
def sample_category(sample_product):
    return Category(
        name="Test Category",
        description="Category description",
        products=[sample_product],
    )


@pytest.fixture(autouse=True)
def reset_category_counters():
    Category.category_count = 0
    Category.product_count = 0
