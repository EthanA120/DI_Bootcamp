# TASK: Responsive CV
from flask import Flask, render_template, redirect, url_for


def main():
    """
        Instructions:
        In this project we will be creating a website which take the users information and creates a nicely styled cv:

            Create a template with a form. The form should have several inputs.
            for example: first name, last name, age, experience etc...

            Create a view that retrieves the data from the form.

            Save the data retrieved in a variable.
            Display the data in a template.

            Bonus: Create multiple styles which the user can choose between for their cv.

    """
    app = Flask(__name__)

    app.config['SECRET_KEY'] = '14ac1c79311cdbe8415062b8151322d7'

    @app.route('/base')
    def base():
        return render_template('base.html', products=retrieve_all_products())

    app.run(debug=True, port=5000)


if __name__ == '__main__':
    main()
