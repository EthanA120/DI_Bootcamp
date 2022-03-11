# TASK: Marketplace
from flask import Flask, render_template
from json import load


def main():
    """
        Look at the pictures below, to understand the assignment

        Instructions:
        Note: For this exercise, we will use the JSON file provided in the assets below.

        This database contains a list of dictionaries. Each dictionary contains these keys:

        ProductId, Category, MainCategory,TaxTarifCode, SupplierName, WeightMeasure
        WeightUnit, Description, Name, ProductPicUrl, Status, Quantity, UoM, CurrencyCode
        Price, Width, Depth, Height, DimUnit

        We will be using these keys to represent each item in our marketplace.
        You don’t have to use all the keys.

        1. Build a marketplace website, the website should have 3 pages:
            1. A homepage, with a welcome message, routed to /.
            2. A products page, that displays a list of all the products that are for sale, routed to /products.
            3. A product details page, that displays the details of the selected product
                (the product id should be passed into the URL), routed to /product/<product_id>


        Asset:
            Download this json file - product_db.json:
                https://github.com/devtlv/studentsGitHub/blob/master/Python%20-%20Part%20Time/Week11/Day4/ExercisesXP/product_db.zip
            To download the json file, click on the “Download Button” or the “View Raw Button”
    """
    app = Flask(__name__)

    with open("Assets/product_db.json", "r") as read_file:
        products_list = load(read_file)
        products_dict = {product["ProductId"]: product for product in products_list}

    @app.route('/base')
    def base():
        return render_template('base.html', products=products_dict)

    @app.route('/')
    @app.route('/homepage')
    def homepage():
        return render_template('homepage.html')

    @app.route('/products')
    def products():
        return render_template('products.html', products=products_dict)

    @app.route('/products/<product_id>')
    def details(product_id):
        return render_template('details.html', products=products_dict, pid=product_id)

    app.run(debug=True, port=5000)


if __name__ == '__main__':
    main()
