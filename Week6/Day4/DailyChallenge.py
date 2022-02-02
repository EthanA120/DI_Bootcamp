import math
from datetime import datetime
import calendar

# TASK: Happy birthday
"""
    1. Ask the user for their birthdate (specify the format, for example: DD/MM/YYYY).
    2. Display a little cake as seen below:

        ___iiiii___
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~

   The number of candles on the cake should be the last number of the users age, if they are 53, then add 3 candles.

    Bonus : If they were born on a leap year, display two cakes !
"""
birthday = input("Enter your birthday (DD/MM/YYYY): ").split("/")
age = (datetime.now() - datetime(day=int(birthday[0]), month=int(birthday[1]), year=int(birthday[2]))).days / 365.2425

age_remainder = math.floor(age) % 10
candles = "_" * math.floor((13 - age_remainder) / 2)
top = candles + "i" * age_remainder + candles

cake = f"""
      {top}
      |:H:a:p:p:y:|
    __|___________|__
   |^^^^^^^^^^^^^^^^^|
   |:B:i:r:t:h:d:a:y:|
   |                 |
   ~~~~~~~~~~~~~~~~~~~
"""

if calendar.isleap(int(birthday[2])):
    print(cake, cake)
else:
    print(cake)
