# TASK: Build a lesson page
import markdown
from flask import Flask
import markdown.extensions.fenced_code


def main():
    """
        Instructions:

        Build a lesson page for the di-learning platform !

        1. Create a directory called lesson1.

        2. Inside the directory there should be 2 markdown files (.md) : in-this-chapter.md and exercises.md.
            The first file in-this-chapter.md should contain a lesson of your choice.
            The second file exercises.md should contain exercises (it can be yours or it can be from the platform).
            Hint: Markdown Crash Course: https://www.youtube.com/watch?v=HUBNt18RFbo
            Check out the markdown documentation: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet

        3. Create 2 routes :
            /exercises will render the exercises.md file
            /lesson will render the in-this-chapter.md file.

        4. BONUS : Display the content of the md files in two different tabs in one HTML file.
    """
    app = Flask(__name__)

    @app.route("/")
    def in_this_chapter():
        readme_file = open("lesson1/in-this-chapter.md", "r")
        md_template_string = markdown.markdown(
            readme_file.read(), extensions=["fenced_code"]
        )
        return md_template_string

    @app.route("/exercise")
    def exercise():
        readme_file = open("lesson1/exercises.md", "r")
        md_template_string = markdown.markdown(
            readme_file.read(), extensions=["fenced_code"]
        )
        return md_template_string

    app.run(debug=True, port=5000)


if __name__ == "__main__":
    main()
