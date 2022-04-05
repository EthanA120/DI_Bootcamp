###What you will create
![What you will create](Instructions.bmp)

---

Explanation: We will create a small project using Flask. The goal will be to render the details of a Pet Store.

This project has 6 different parts
<pre>
├── PetStore/ 
│    ├── app/
│       ├── __init__.py
│       ├── routes.py
│       ├── models.py
│       └── templates/ 
│            ├── index.html
│            ├── pets.html
│            ├── pet.html
│            ├── cart.html
└── run.py
</pre>

---

###Part I: Database and models

1. Create a new folder called PetStore.


2. Create a folder called app : most of our files will be within the app folder.


3. In the app folder create a __init__.py file and use app.config to configure the Database. Let’s call our Database petstore.


4. Create a file called models.py:
   - Use SQLAchemy to create a model called Pet. This model should have the following columns:
      - id : A Primary key
      - name : the name of the animal (String, unique)
      - gender : the gender of the animal (String - or M or F)
      - breed : the breed of the animal (String)
      - date_of_birth : the date of birth of the animal (Date, default : today)
      - details : some important detail about the animal (Text)
      - price : the price of the animal (Integer)
      - image : the image URL of the animal (String)


5. Use Flask Migrate to create the petstore Database including the Pet table.


6. Manually add some pets to the table.

---

###Part II : Routes

In the app folder, create the routes.py file with the three following routes:
1. index route : / linked to the index.html template (see below)

2. pets route : /pets linked to the pets.html template (see below)

3. specific pet route : /pet/\<int:pet_id> : linked to the pet.html template (see below)

---

###Part III: Templates

1. In the app folder, create a templates folder with four files.
   1. index.html is the menu, with a navbar. Each link will redirect the user to the appropriate page. On this template add some details about your website.
           You could use an [API](https://alexwohlbruck.github.io/cat-facts/docs/endpoints/facts.html) to display some facts about cats 😉
   
   2. pets.html is where the most important details of all the animals will be rendered: name, breed, price and image.
      - Add a button next to each pet, that will redirect the user to the /pet/\<int:pet_id> route.
      
   3. pet.html is where all the details of the chosen pet will be rendered.
      - Add a button next to each pet, that will redirect the user to the /add_pet/\<int:pet_id> route. (see below Part IV)
      
   4. cart.html is the user’s cart. It should contain all the added pets. (see below Part IV)


2. Style your website : Use template inheritance, CSS and Bootstrap

---

Part IV: Cart

1. In the models.py file:
   1. Use SQLAchemy to create a model called Cart. This model should have the following fields:
      - id : A Primary key
      - pets : (see below the details of the relationships)

   2. There is a One-To-Many relationship between the Pet model and the Cart model : a cart can contain many pets, but a pet can only belong to one cart. <br>
   What should be added to the models of the models.py file to represent this relationship?

   3. Add a few methods to the Cart class:
      1. add_to_cart(self, pet_id) : adds the id of the selected pet to the Cart table.
      2. get_cart(self) : gets all the data from the Cart table and returns it (ie. a class method).
      3. get_total(self) : calculates the total amount ($) of the cart and returns it.

    
2. Create a few more routes in routes.py :
   1. /add_pet/\<int:pet_id> : adds the specific pet to the cart. As soon as the pet is added to the cart, redirect the user to the pets.html page.

   2. /cart : linked to the cart.html template.

---

Part V: Bonus I

1. Add a button in the templates pet.html and cart.html that redirects the user to the template pets.html.
2. Add a flash message as soon as a new pet is added to the cart.
3. Create error pages and implement them wherever you think it’s needed.
4. Add a new field to the Cart model : number_of_pets.
   - Therefore, the user can add the same pet multiple times.
   - In the cart, next to each pet add a “+” and “-” button that triggers the number_of_pets field.

---

Part VI: Bonus II

1. In the models.py file, create a new model called Country with the following fields:
   - id : a Primary key
   - name : the name of the country (String, unique) <br>
   It should have a Many-To-Many relationship with the Pet model. A pet can be found in several countries (ie. country of origin), and a country can have multiple pets.<br>
   What should you add in the Pet model to represent this relationship? Should you create an association table?

2. You can use the faker module to populate the country table.

3. We want to add a country of origin to each pet. Therefore, using a function, randomly add one or several country id’s to each pet that exists in the pet table. In which table should this be implemented?

4. In the class Pet and in the file routes.py, add a few python methods/functions which will render the pets depending on their country of origin. In the template, sort the pets alphabetically depending on their names.

5. We want the project to be more userfriendly. On the pets.html template add a search form to search for a specific country name. It should filter the pets on the page. When the form is empty, the page should render all the pets.

