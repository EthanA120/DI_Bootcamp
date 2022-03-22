# TASK: Responsive CV
from secrets import token_hex
from forms import UserDetails
from flask import Flask, render_template, redirect, url_for, request


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

    s_key = token_hex(16)
    app.config["SECRET_KEY"] = s_key
    print(s_key, app.config["SECRET_KEY"])

    @app.route('/')
    @app.route('/create', methods=["POST", "GET"])
    def create():
        form = UserDetails()
        return render_template('create.html', title='Create CV', form=form)

    @app.route('/cvpage', methods=["GET", "POST"])
    def cvpage(user_name, user_details):
        return render_template('cvpage.html', title='CV Page', user_name=user_name, user_details=user_details)

    @app.route('/assist', methods=["POST", "GET"])
    def assist(form):
        user_details = {}
        print(request.method)
        print(form.validate_on_submit())
        print(form.errors)
        user_details['first'] = form.first_name.data
        user_details['last'] = form.last_name.data
        user_details['hobbies'] = form.hobbies.data
        user_details['strengths'] = form.strengths.data
        user_details['weaknesses'] = form.weaknesses.data
        return redirect(url_for('cvpage',
                                user_name=f"{user_details['first']}{user_details['last']}",
                                user_details=user_details)
                        )

    app.run(debug=True, port=5000)


if __name__ == '__main__':
    main()
