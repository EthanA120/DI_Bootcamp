# TASK: Exercise 1
"""
    Choose any function you wrote in the functions chapter and store it in a separate file then use import with the following syntaxes:

    import module_name
    from module_name import function_name
    from module_name import function_name as fn
    import module_name as mn
"""
# import string
# from Week7.Day2.XPGold import set_season
# from Week7.Day2.XPGold import get_random_temp as grt
# import datetime as dt


# TASK: Exercise 2
from random import randint

def one_to_hundred():
    """
        Create a function that accepts a number between 1 and 100, then rolls a random number between 1 and 100,
        if it’s the same number, display a success message to the user, else don’t.
    """
    num = int(input("Enter a number between 1 and 100: "))
    rnd_num = randint(1, 100)
    if num == rnd_num:
        print("Success!")


# TASK: Exercise 3
import random
import string

def random_string():
    """
        Generate random String of length 5
        Note: String must be the combination of the UPPER case and lower case letters only. No numbers and a special symbol.
        Hint: use the string module
    """
    for i in range(5):
        print(random.choice(random.choice(string.ascii_letters)), end="")


one_to_hundred()
random_string()