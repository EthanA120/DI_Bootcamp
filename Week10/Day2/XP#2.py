from datetime import datetime
from dateutil.relativedelta import relativedelta
import holidays
from faker import Faker


# TASK: Exercise 1
def display_today(display=False):
    """
        Create a function that displays the current date.
        Hint : Use the datetime module.
    """
    this_day = datetime.today()
    if display:
        print(this_day.strftime("%d-%b-%Y"))
    return this_day


# TASK: Exercise 2
def jan_delta():
    """
        Create a function that displays the amount of time left from now until January 1st.
        (Example: the 1st of January is in 10 days and 10:34:01hours).
    """
    delta_time = display_today() - datetime.strptime('01-01-2022', "%d-%m-%Y")
    print(delta_time)


# TASK: Exercise 3
def minutes_of_life(birthday, display=False):
    """
        Create a function that accepts a birthdate as an argument (in the format of your choice),
        then display a message stating how many minutes the user has been alive.
    """
    birthday = datetime.strptime(birthday, "%d/%m/%Y")
    age = (display_today() - birthday)
    if display:
        print(f"It's been {round(age.total_seconds() / 60, 2)} minutes since you were born")
    return age


# TASK: Exercise 4
def till_next_holiday():
    """
        1. Write a function that display today’s date.
        2. The function should also display the amount of time left from now until the next upcoming holiday and print which holiday that is.
            Example: the next holiday is in 30 days and 12:03:45 hours.
        Hint: Start by hard coding the datetime and name of the upcoming holiday.
    """
    this_day = display_today()
    next_holiday = this_day
    israel_holidays = holidays.country_holidays('IL')

    while next_holiday not in israel_holidays:
        next_holiday += relativedelta(days=1)
    holiday_name = israel_holidays.get(next_holiday)
    print(f"Next holiday is going to be {holiday_name} and it will be at {next_holiday:%d/%m/%Y}")


# TASK: How Old Are You On Jupiter?
def age_on_jupiter(age, planet):
    """
        Given an age in seconds, calculate how old someone would be on:
            - Earth: orbital period 365.25 Earth days, or 31557600 seconds
            - Mercury: orbital period 0.2408467 Earth years
            - Venus: orbital period 0.61519726 Earth years
            - Mars: orbital period 1.8808158 Earth years
            - Jupiter: orbital period 11.862615 Earth years
            - Saturn: orbital period 29.447498 Earth years
            - Uranus: orbital period 84.016846 Earth years
            - Neptune: orbital period 164.79132 Earth years

        So if you are told someone is 1,000,000,000 seconds old,
        the function should output that they are 31.69 Earth-years old.
    """
    planet = planet.title()
    earth_years_in_secs = 3.16887646e-8
    planets_year = {
        "Earth": 1,
        "Mercury": 0.2408467,
        "Venus": 0.61519726,
        "Mars": 1.8808158,
        "Jupiter": 11.862615,
        "Saturn": 29.447498,
        "Uranus": 84.016846,
        "Neptune": 164.79132,
    }
    print(age * earth_years_in_secs * planets_year[planet])


# TASK: Faker Module
def add_dict(user_list):
    """
    1. Install the faker module, and take a look at the documentation and learn how to properly implement faker in your code.
    2. Create an empty list called users.
        Tip: It should be a list of dictionaries.
    3. Create a function that adds new dictionaries to the users list.
        Each user has the following keys: name, address, language_code. Use faker to populate them with fake data.
    """
    fake = Faker()
    user_list.append({"name": fake.name(), "address": fake.address(), "language_code": fake.language_code()})
    print(user_list)


display_today(True)
jan_delta()
minutes_of_life("10/10/1993", True)
till_next_holiday()
age_on_jupiter(minutes_of_life("10/10/1993").total_seconds(), "Earth")
add_dict([])

