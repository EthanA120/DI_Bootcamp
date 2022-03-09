# TASK: DailyChallengeColors
from flask import Flask, render_template


def main():
    """
        In this exercise we will be creating a website which provides a list of colors.
        When the user, clicks on a color, it will direct him to a page with that background color.

        Create a website with two pages:
            1. Homepage: This page should have a navbar with a list of colors.
                (Use the navbar provided below in the assets.)
            2. Color: This page will be a blank page with only a background color.

    """
    app = Flask(__name__)

    @app.route('/')
    def homepage():
        return render_template('Homepage.html')

    @app.route('/<back_color>')
    def color(back_color):
        return render_template('Color.html', background_color=back_color)

    app.run(debug=True, port=5000)


if __name__ == '__main__':
    main()
