from json import load


def retrieve_all_products():
    with open("static/products.json", "r") as read_file:
        all_products = load(read_file)
    return all_products


def retrieve_requested_product(product_id: str):
    requested_product = next(product for product in retrieve_all_products() if product["ProductId"] == product_id)
    return requested_product
