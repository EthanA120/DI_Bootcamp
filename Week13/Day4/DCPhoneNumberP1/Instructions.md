##Instructions : Phone number

###Hint
- Check out [this tutorial](https://www.twilio.com/blog/a-phone-number-input-field-for-flask-forms) explaining how to create a complete application using Flask and phone numbers.
- Check out [this video](https://www.youtube.com/watch?v=juPQ04_twtA) about One-to-Many relationship with Flask and SqlAlchemy

---

This exercise is divided into 2 parts today we will be doing part 1 and tomorrow we will do part 2.

---

Create a 411 (114 in Israel) website that allows you to search for people depending on their phone numbers.

The database should have two tables :

A table called Person with the following attributes:

    id (Integer, Primary Key)
    name (String)
    email (String, unique)
    phonenumbers (relationship)
    address (String)

A table called Phonenumber with the following attributes:

    id (Integer, Primary Key)
    number (String)
    owner (Foreign Key)


Here is what you need to implement:

1. The **Person** table should have a One-To-Many relationship with the **Phonenumber** table : a person can have many phone numbers, although a phone number belongs to only one person.

2. Use the faker module to add some records to the Person table. Use the [person provider](https://faker.readthedocs.io/en/master/providers/faker.providers.person.html) and the [address provider](https://faker.readthedocs.io/en/master/providers/faker.providers.address.html).

3. You also need to add some records to the Phonenumber table:
        Use faker to add the numbers . Use the phone_number provider.
        In the *owner* column, randomly link a person to a phone number (ie. first, retrieve a person randomly from the Person table, then assign it to a Phonenumber record).

4. Create a view whose route is *"/person/<phonenumber>"* that will display all the info of a person depending on their phone number.

5. Create a view whose route is *"/person/<name>"* that will display all the info of a person depending on their name. Don’t forget to display their phone number(s) as well.

6. In parts 4 and 5 if there is no results display a message saying no results found.
