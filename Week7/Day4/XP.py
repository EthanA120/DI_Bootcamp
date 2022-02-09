# TASK: When will I retire ?
"""
    The point of the exercise is to check if a person can retire depending on their age and their gender.
    Note : Retirement age in Israel is 67 for men, and 62 for women (born after April 1947).

    1. Create a function get_age(year, month, day) Hard-code the current year and month in your code
        (there are better ways of doing this, but for now it will be enough.)
    2. After calculating the age of a person, the function should return the age (the age is an integer).
    3. Create a function can_retire(gender, date_of_birth).
        It should call the get_age function (with what arguments?) in order to receive an age.
        Now the information we have is sufficient to determine if the person is able to retire or not.
    4. Calculate. You may need to do a little more hard-coding here.
    5. Return True if the person can retire, and False if he/she can't.

    Some Hints:
    1. Ask for the user's gender as "m" or "f".
    2. Ask for the user's date of birth in the form of "yyyy/mm/dd", eg. "1993/09/21".
    3. Call can_retire to get a definite value for whether the person can or can't retire.
    4. Display a message informing the user whether they can retire or not.
        As always, test your code to ensure it works.
"""
from datetime import datetime


def get_age(year, month, day):
    birthday = datetime(day=int(day), month=int(month), year=int(year))
    return (datetime.now() - birthday).days / 365.2425


def can_retire(gender, date_of_birth):
    age = get_age(date_of_birth[2], date_of_birth[1], date_of_birth[0])

    if gender in ["m", "male"] and age >= 67 or gender in ["f", "female"] and age >= 62:
        return True
    else:
        return False


birthdate = input("Enter your birthday (DD/MM/YYYY): ").split("/")
sex = input("Are you male or female: ").lower()

if can_retire(sex, birthdate):
    print("Congrats! you can retire :)")
else:
    print("You are young and strong, you can't retire yet.")


# TASK: Exercise 8
"""
    Write a function that accepts one parameter (an int: X) and returns the value of X+XX+XXX+XXXX.

    Example:
        If X=3, the output when calling our function should be 3702 (3 + 33 + 333 + 3333)
    
    Hint: treating our number as a int or a str at different points in our code may be helpful
"""
x = input("What should be the value of X? ")

total = 0
for i in range(1, 5):
    total = eval("total + " + i*x)

print(total)
