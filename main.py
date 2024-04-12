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

def price_change_last_month(products, product_name):
    """
    Calculates the price change of a product for the last month.

    Args:
        products (list): A list of dictionaries representing products.
        product_name (str): The name of the product.

    Returns:
        str: A message indicating the price change for the product in the last month.
    """
    today = datetime.now()
    last_month = today - timedelta(days=30)

    relevant_prices = [product['price'] for product in products if product['name'] == product_name and product['date'] >= last_month]
    if len(relevant_prices) < 2:
        return f"Not enough data to calculate price change for {product_name} in the last month."

    initial_price = relevant_prices[0]
    final_price = relevant_prices[-1]
    price_change = final_price - initial_price
    percentage_change = (price_change / initial_price) * 100

    return f"The price change for {product_name} in the last month: {price_change:.2f} ({percentage_change:.2f}%)"

def write_to_file(file_name, content):
    """
    Writes content to a file.

    Args:
        file_name (str): The name of the file to write the content to.
        content (str): The content to be written to the file.
    """
    with open(file_name, "w") as file:
        file.write(content)
    print("Result saved to result.txt")

if __name__ == "__main__":
    file_name = "products.txt"
    products = read_products_file(file_name)

    processed_products = set()  # To keep track of processed products
    result_content = ""

    for product in products:
        if product['name'] not in processed_products:
            result = price_change_last_month(products, product['name'])
            result_content += f"{result}\n"
            processed_products.add(product['name'])

    write_to_file("result.txt", result_content)
