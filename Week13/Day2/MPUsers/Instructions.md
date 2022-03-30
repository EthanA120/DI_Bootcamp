###Exercise 1: Users
Instructions

In this exercise you will:
- populate a table with data from a json file.
- display the table data in a template
- add new users to the table

You will be using this [_json file_](https://jsonplaceholder.typicode.com/users).

---
Useful Resources 
- [Select, Insert, Delete flask-sqlalchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/queries/#inserting-records)

---

###Part I

1. Create a new directory for this project.
2. Download the json file given above (Right click -> Save As), and save it inside your new directory.

3. Create an ___init__.py_ file.
    1. Use _app.config_ to configure the Database. Let’s call our database _robots_ (because the json file contains a list of robots 😉)
    2. Add the following lines:<br>
    `from flask import Flask` <br>
    `from flask_sqlalchemy import SQLAlchemy` <br>
    `from flask_migrate import Migrate` <br>

    3. Then add two new objects
      - A _db_ object that represents the database.
      - An object that represents the migration engine.

4. Create a file called _models.py_
    1. Use SQLAchemy to create a _User_ Class (i.e. our _User_ model). This model should have a few columns :
       - id : a primary key
       - name : a String
       - street : a String
       - city : a String
       - zipcode : a String

    2. Use Flask Migrate to add this new table to the database
        Create the migration repository by running this command in the terminal: _flask db init_.
        After you run this command, you will find a new migrations directory.
        To generate automatic migrations, run this command in the terminal _flask db migrate -m "user table"_
        To apply the changes to the database, run this command in the terminal _flask db upgrade_.
        The _upgrade_ command will detect that a database does not exist and will create it.

5. In the __init__.py file:
   1. Create a function named populate(), that will populate the User table with the user’s data from the json file. (Be careful, only populate the columns with the fields : name, address street, address city, address zipcode)
   2. Call the function **once**.

---
###Part II

1. Create a file called routes.py, and add a new route / . The view function of this route returns the index.html template (see below).

2. Create a templates folder, with an index.html file. The users from the User table will be displayed on this template. Create a new <div> for each instruction below:
   1. Display all the users (with all the details).
   
   2. Only display the user(s) who live(s) in “Roscoeview”.
   Tip: It should only display the user “Chelsey Dietrich”

   3. Only display the first 5 users.

   4. Only display the user(s) which zipcode starts with the number 5.
   Tip: It should display the users “Clementine Bauch”, “Patricia Lebsack”, “Kurtis Weissnat”

---
###Part III - Bonus

1. Create a file called _forms.py_ that will hold our “AddUser” form. This form should have a few inputs:
   - user_name : StringField
   - street : StringField
   - city : StringField
   - zipcode : StringField
   - a button : SubmitField
   - You can add some validators to the form fields if you want :)

2. In the templates folder, create a file _add_user.html_. This template contains the form created above.

3. In the _routes.py_ file, add a new route:
   - Route _/add_user_ : this route is linked to the _add_user.html_ template.
     - If the submit button was clicked and the form filled, retrieve the form data, and add the new user to the _User_ table. If everything went well (ie. without any errors - use Exception Handling) you should be redirected to the _/_ route.
     - else, render the form