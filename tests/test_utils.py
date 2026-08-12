from src.utils import CategoryIterator


def test_category_iterator(sample_category, sample_product):
    products = list(CategoryIterator(sample_category))
    assert products == [sample_product]