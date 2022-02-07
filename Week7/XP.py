# TASK: What are you learning ?
"""
    1. Write a function called display_message() that prints one sentence telling what you are learning in this course.
    2. Call the function, and make sure the message displays correctly.
"""
def display_message():
    print("In this course I learn how to develop websites\n")


display_message()


# TASK: What’s your favorite book?
"""
    1. Write a function called favorite_book() that accepts one parameter called title.
    2. The function should print a message, such as "One of my favorite books is Alice in Wonderland".
    3. Call the function, make sure to include a book title as an argument when calling the function.
"""
def favorite_book(title):
    print(f"One of my favorite books is {title}\n")


favorite_book("Alice in Wonderland")


# TASK: Some Geography
"""
    1. Write a function called describe_city() that accepts the name of a city and its country as parameters.
    2. The function should print a simple sentence, such as "Reykjavik is in lceland".
    3. Give the country parameter a default value.
    4. Call your function.
"""
def describe_city(city="Jerusalem", country="Israel"):
    print(f"{city} is in {country}\n")


describe_city()


# TASK: Random
"""
    Create a function that accepts a number between 1 and 100 and generates another number randomly between 1 and 100.
    Compare the two numbers, if it’s the same number, display a success message,
    otherwise show a fail message and display both numbers.
"""
from random import randint


def random_num(user_num):
    rand_num = randint(1, 101)

    if rand_num == user_num:
        print("Success!")
    else:
        print(f"It's a failure, your number: {user_num}, computer number: {rand_num}\n")


random_num(int(input("Enter a number from 1 to 100: ")))


# TASK: Let’s create some personalized shirts!
"""
    1. Write a function called make_shirt() that accepts a size and a text that should be printed on the shirt.
    2. The function should print a sentence summarizing the size of the shirt and the message printed on it.
    3. Call the function make_shirt() using positional arguments to make a shirt.
    4. Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python.
    5. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.
    6. Bonus: Call the function make_shirt() using keyword arguments.
"""
def make_shirt(size="L", text="I love Python"):
    print(f'The shirt size is {size} and it says: "{text}"')


make_shirt("M", "I learn pyton")
make_shirt()
make_shirt("M")
make_shirt(text="I learn pyton")
make_shirt(text="I learn pyton\n", size="M")


# TASK: Magicians...
"""
    1. Make a list of magician's names
    2. Pass the list to a function called show_magicians(), which prints the name of each magician in the list.
    3. Write a function called make_great(),
        the function modifies the list of magicians by adding the phrase "the Great" to each magician's name.
    4. Call the function make_great().
    5. Call the funcyion show_magicians() to see that the list has actually been modified.
"""
def show_magicians(magic_list):
    [print(magician) for magician in magicians]


def make_great(magic_list):
    for i, magician in enumerate(magicians):
        magicians[i] = "the Great " + magician


magicians = ["David Copperfield", "Doug Henning", "Lance Burton", "Ricky Jay", "Mark Wilson"]
make_great(magicians)
show_magicians(magicians)
