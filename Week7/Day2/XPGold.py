# TASK: Temperature Advice
"""
    1. Create a function called get_random_temp().
        1. This function should return an integer between -10 and 40 degrees (Celsius), selected at random.
        2. Test your function to make sure it generates expected results.

    2. Create a function called main().
        1. Inside this function, call get_random_temp() to get a temperature, and store its value in a variable.
        2. Inform the user of the temperature in a friendly message,
            e.g. "The temperature right now is 32 degrees Celsius."
            
    3. Let's add more functionality to the main() function. Write some friendly advice relating to the temperature:
        1. below zero (e.g. "Brr, that's freezing! Wear some extra layers today")
        2. between zero and 16 (e.g. "Quite chilly! Don't forget your coat")
        3. between 16 and 23
        4. between 24 and 32
        5. between 32 and 40

    4. Change the get_random_temp() function:
        1. Add a parameter to the function, named 'season'.

        2. Inside the function, instead of simply generating a random number between-10 and 40,
            set lower and upper limits based on the season,
            e.g. if season is 'winter', temperatures should only fall between -10 and 16.

        3. Now that we've changed get_random_temp(), let's change the main() function:
            1. Before calling get_random_temp(), we will need to decide on a season,
                so that we can call the function correctly. Ask the user to type in a season - 'summer', 'autumn'
                (you can use 'fall' if you prefer), 'winter, or 'spring'
            2. Use the season as an argument when calling get _random_temp().

    5. Bonus: Give the temperature as a floating-point number instead of an integer.

    6. Bonus: Instead of asking for the season, ask the user for the number of the month (1 = January, 12 = December).
        Determine the season according to the month.
"""
from random import uniform
from datetime import datetime


def get_random_temp(season):
    if season == "Winter":
        return uniform(-10, 24)
    elif season == "Spring":
        return uniform(16, 32)
    elif season == "Summer":
        return uniform(24, 41)
    elif season in ["Autumn", "Fall"]:
        return uniform(18, 34)


def set_season(month):
    spring = ["March", "April", "May"]
    summer = ["June", "July", "August"]
    autumn = ["September", "October", "November"]
    winter = ["December", "January", "February"]

    if month not in spring + summer + autumn + winter:
        month = datetime.strftime(datetime.now(), "%B")

    if month in spring:
        return "Spring"
    elif month in summer:
        return "Summer"
    elif month in autumn:
        return "Autumn"
    elif month in winter:
        return "Winter"


def main():
    month = input("Enter a month: ").title()
    season = set_season(month)

    random_temperature = round(get_random_temp(season), 2)
    print(f"The temperature right now is {random_temperature} degrees Celsius.")

    if random_temperature < 0:
        print("Brr, that's freezing! Wear some extra layers today")
    elif 0 <= random_temperature < 16:
        print("Quite chilly! Don't forget your coat")
    elif 16 <= random_temperature < 23:
        print("Nice weather outside! Great for being productive")
    elif 23 <= random_temperature < 32:
        print("It's a bit warm! Good weather for picnic")
    else:
        print("Oh it's hot! It's a great weather for swimming")


main()
