import pytest
from datetime import datetime, timedelta
from main import read_products_file, price_change_last_month

@pytest.fixture
def sample_products_file(tmp_path):
    """
    Fixture to create a sample products file for testing.

    Args:
        tmp_path: A temporary directory provided by pytest.

    Returns:
        str: Path to the created sample products file.
    """
    # Create a sample products file for testing
    file_content = """Product1, 2024-03-15, 105.0
Product1, 2024-04-05, 115.0
Product2, 2024-03-15, 200.00
Product3, 2024-03-16, 50.00
Product2, 2024-04-05, 100.00
Product3, 2024-04-03, 200.00"""
    file_path = tmp_path / "products.txt"
    with open(file_path, 'w') as file:
        file.write(file_content)
    return file_path

def test_read_products_file(sample_products_file):
    """
    Test the read_products_file function.

    Args:
        sample_products_file: Path to the sample products file.

    Returns:
        None
    """
    expected_products = [
        {'name': 'Product1', 'date': datetime(2024, 3, 15), 'price': 105.0},
        {'name': 'Product1', 'date': datetime(2024, 4, 5), 'price': 115.0},
        {'name': 'Product2', 'date': datetime(2024, 3, 15), 'price': 200.0},
        {'name': 'Product3', 'date': datetime(2024, 3, 16), 'price': 50.0},
        {'name': 'Product2', 'date': datetime(2024, 4, 5), 'price': 100.0},
        {'name': 'Product3', 'date': datetime(2024, 4, 3), 'price': 200.0}
    ]
    assert read_products_file(sample_products_file) == expected_products

@pytest.mark.parametrize("product_name, expected_result", [
    ("Product1", "The price change for Product1 in the last month: 10.00 (9.52%)"),
    ("Product2", "The price change for Product2 in the last month: -100.00 (-50.00%)"),
    ("Product3", "The price change for Product3 in the last month: 150.00 (300.00%)"),
    ("NonexistentProduct", "Not enough data to calculate price change for NonexistentProduct in the last month.")
])
def test_price_change_last_month(sample_products_file, product_name, expected_result):
    """
    Test the price_change_last_month function.

    Args:
        sample_products_file: Path to the sample products file.
        product_name: Name of the product.
        expected_result: Expected result string.

    Returns:
        None
    """
    products = read_products_file(sample_products_file)
    assert price_change_last_month(products, product_name) == expected_result
