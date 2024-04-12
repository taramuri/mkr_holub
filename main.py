from datetime import datetime, timedelta

def read_products_file(file_name):
    """
    Reads product data from a file.

    Args:
        file_name (str): The name of the file containing product data.

    Returns:
        list: A list of dictionaries representing products, each containing 'name', 'date', and 'price' keys.
    """
    products = []
    with open(file_name, 'r') as file:
        for line in file:
            product_data = line.strip().split(',')
            if len(product_data) == 3:
                products.append({
                    'name': product_data[0].strip(),
                    'date': datetime.strptime(product_data[1].strip(), '%Y-%m-%d'),
                    'price': float(product_data[2].strip())
                })
    return products
