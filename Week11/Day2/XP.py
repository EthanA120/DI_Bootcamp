# TASK: Exercise 1
import flask


def ex1():
    """
        Instructions
            1. Use pip to install the flask module.
            2. Run the command import flask in a python shell.
            3. Run the command dir(flask) to see the different methods that come along with flask.
    """
    print(dir(flask))


# TASK: Exercise 2
def ex2():
    """
        Using Flask, create a template for your CV.
        Your CV should contain:

            - Your name
            - A picture
            - Your hobbies
            - Your skills
            - Your strengths
            - Your weaknesses

            Bonus: Add some CSS
            Hint : To add some CSS take a look at the video called Static Files in the Online Learning section.
    """
    app = flask.Flask("index")

    @app.route("/")
    def cv_format():
        name = "Ethan"
        pic = "https://e7.pngegg.com/pngimages/211/121/png-clipart-piano-musical-instrument-musical-note-keyboard-piano-painted-hand.png"
        hobbies = "Flying, Computing, Dreaming"
        skills = "Annoying, Playing, Time traveling"
        strengths = "Perfectionist, Can touch the nose with the tongue"
        weaknesses = "Perfectionist, Can't touch the elbow with the tongue"

        body = r"{font-family: Arial;}"
        h12 = r"{text-align: center;}"
        h2 = r"{color: #3D5AFE;}"
        p = r"{font-size: 1.3em;}"
        return f"""
        <!DOCTYPE html>
        <html lang=”en”>
            <head>
                <meta charset=”UTF-8">
                <title>ABOUT</title>
            </head>
            <style>
                body{
                    body
                }
                h1, h2{
                    h12
                }
                h2{
                    h2
                }
                p{
                    p
                }
                
            </style>
            <body>
                <h1>Your CV:</h1>
                    <h2>Your name: {name}</h2><br>
                    <img src={pic} width="200" height="120" style="margin: auto; display: block;"><br>
                    <p>Your hobbies: {hobbies}</p><br>
                    <p>Your skills: {skills}</p><br>
                    <p>Your strengths: {strengths}</p><br>
                    <p>Your weaknesses: {weaknesses}</p><br>
            </body>
        </html>
        """

    app.run(debug=True, port=5000)


if __name__ == '__main__':
    ex1()
    ex2()
