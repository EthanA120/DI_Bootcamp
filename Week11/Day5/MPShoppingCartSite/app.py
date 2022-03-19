# TASK: Shopping cart site
import json
from forms import AddItem
from flask import Flask, render_template, redirect, url_for, request, flash
from products_data import retrieve_all_products, retrieve_requested_product


def main():
    """
        Instructions:
            - Today we are going to be creating a website that allows the users to add and delete items from their shopping cart.
            - In the assets below, you can find a json file containing all the products you will be using for your store
            - Don’t forget to download the img zip found below in the assets.
                (these images should be placed in you static folder)
            - As a reminder, look at the assets below for the Lesson on Python File I/O
                (reading and writing from a json file)

        Assets:
        - Products file here:
            https://raw.githubusercontent.com/devtlv/studentsGitHub/master/Python/Week6/ProjectFlaskPythonPartTime/products.json
        - To save the json file you should : –> right-click, save link as…
        - Download also the img zip here:
            https://github.com/devtlv/studentsGitHub/blob/master/Python%20-%20Part%20Time/Week11/Day5/Mini%20Project/img.zip
        - Lesson on Python File I/O here:
            http://learn.di-learning.com/courses/collection/30/course/125/section/381/chapter/335

        Project structure:
        Part I:
            1. Create a file named products_data.py.
                1. Create a function named retrieve_all_products that should read all the products from the json file,
                    and return it in a variable called all_products

                2. Create a second function named retrieve_requested_product that takes the product id of the selected product as a parameter (from the products' template - see below).
                This function should read all the products from the json file, and return the product with the same id as the given parameter.
                Save the product in a variable called requested_product.

            2. Add an app.py file to your project.
                1. In this file, we will be using the functions written in the products_data.py. How can we access these?
                2. Create a route with the following URL /, that will trigger a function that returns the template that welcomes the user, and tells them about your store.
                3. Create a route with the following URL /products, that will trigger a function that returns a template that displays all the products.
                    Each product should have a button that directs the user to the /products/<product_id> URL.
                4. Create a route with the following URL /products/<product_id>, that will trigger a function that returns a template that displays the requested product. The product should have a button that allows the user to add this product to his cart.


        Part II:
            At this point, we will be creating the functionality that allows the user to add and delete products from their cart.

            1. In the app.py file
                1. Create a route with the following URL /cart that leads to the cart template
                    (it should display all the products in the cart with their price, the total price and a button next to each product that allows the user to delete it from his cart)
                2. Create a variable named cart_item.
                    This variable will hold all the products added to the cart.
                3. Create a route with the following URL /add_product_to_cart/<product_id> that triggers a function.
                    This function should take the product id as a parameter, and append the product details to the cart_item variable.
                4. Create a route with the following URL /delete_product_from_cart/<product_id> that triggers a function.
                    This function should take the product id as a parameter, and delete the product details from the cart_item variable.
                    Note : If you feel comfortable with json, you could write the products into a cart.json file


        Part III: BONUS
        At this point, we will be creating the functionality that allows the user to sign up and login to our store website.
        This part is advanced. You need to teach yourself flask forms.

        1. Create a new json file named users.json. The json file will contain a list of dictionaries. Each dictionary contains the user’s name, email and password.
        2. Create a file named user_data.py.
            1. Create a function named add_user that appends the user to the json file.
            2. Create a function named check_user that checks the user’s credentials.
                - If the user’s credentials exist in the json file, redirect the user to the homepage.
                - If not, redirect the user to the sign-up page.
        3. In the app.py file,
            1. Create a signup view. It should retrieve the data from the signup form and call the add_user function.
            2. Create a login view. It should retrieve the data from the login form and call the check_user function.
                Note: Keep someone logged in by using flask sessions, this will keep track of the current user.

    """
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '04ac1c79311cdbe8415062b8151322d7'

    @app.route('/base')
    def base():
        return render_template('base.html', products=retrieve_all_products())

    @app.route('/')
    @app.route('/homepage')
    def homepage():
        return render_template('homepage.html', title='Homepage')

    @app.route('/products', methods=["POST", "GET"])
    def products():
        form = AddItem()
        return render_template('products.html', title='Products', products=retrieve_all_products(), form=form)

    @app.route('/products/<product_id>')
    def details(product_id):
        return render_template('details.html', title=product_id, product=retrieve_requested_product(product_id))

    @app.route('/cart')
    def cart(cart_item):
        return render_template('cart.html', title='Cart', cart_item=cart_item)

    @app.route('/add_product_to_cart/<product_id>')
    def add_to_cart(product_id, qty=0):
        with open('static/cart.json', 'w+') as w_r_file:
            cart_list = json.load(w_r_file)
            if product_id in cart_list.keys():
                cart_list[product_id]["qty"] += qty
            else:
                cart_list[product_id] = product_id
            json.dump(cart_list, w_r_file, indent=2, sort_keys=True)

    @app.route('/delete_product_from_cart/<product_id>')
    def delete_from_cart():
        pass

    app.run(debug=True, port=5000)


if __name__ == '__main__':
    main()
