# TASK: Birthday Look-up, TASK: Birthdays Advanced, TASK: Add Your Own Birthday
"""
    1. Create a variable called birthdays. Its value should be a dictionary.

    2. Initialize this variable with birthdays of 5 people of your choice.
        For each entry in the dictionary, the key should be the person's name, and the value should be their birthday.
        Tip: Use the format "YYYY/MM/DD".

    3. Print a welcome message for the user. Then tell them: "You can look up the birthdays of the people in the list!"
        1. Ask the user to give you a person's name and store the answer in a variable.
        2. Get the birthday of the name provided by the user.
        3. Print out the birthday with a nicely-formatted message.

    4. Birthdays Advanced:
        1. Before asking the user to input a person’s name print out all of the names in the dictionary.
        2. If the person that the user types is not found in the dictionary,
            print an error message (“Sorry, we don’t have the birthday information for <person’s name>”)

    5. Add Your Own Birthday:
        1. Add this new code:
            before asking the user to input a person's name to look up, ask the user to add a new birthday:
            1. Ask the user for a person's name store it in a variable.
            2. Ask the user for this person's birthday (in the format "YYYY/MM/DD") - store it in a variable.
            3. Now add this new data into your dictionary.
        2. Make sure that if the user types any name that exists in the dictionary - including the name that he entered himself - the corresponding birthday is found and displayed.
"""
from datetime import datetime

birthdays = {
    "einstein": datetime(1879, 3, 14),
    "bohr": datetime(1885, 10, 7),
    "wigner": datetime(1902, 11, 17),
    "feynman": datetime(1918, 5, 11),
    "yonath": datetime(1993, 6, 22)
}

print("Welcome! \nYou can look up the birthdays of the people in the list:")
[print(key.title()) for key in birthdays.keys()]

new_name = input("Enter a name of a person: ").lower()
new_date = input("Enter the birthday of this person (YYYY/MM/DD): ")
birthdays[new_name] = datetime.strptime(new_date, "%Y/%m/%d")

person_name = input("Enter a person's name to get his birthday: ").lower()

if person_name in birthdays.keys():
    print(f"{person_name.title()} was born on {datetime.strftime(birthdays[person_name], '%d %B, %Y')}")
else:
    print(f"Sorry, we don’t have the birthday information for {person_name}")


# TASK: Fruit Shop
"""
    1. Create a new dictionary called items and populate the dictionary with the following key value pairs,
        each pair represents an item and its price.
        "banana": 4,
        "apple": 2,
        "orange": 1.5,
        "pear": 3
    2. Print all the items and their prices in a sentence.
    3. Change the value of all the keys to dictionaries containing both the price and the amount of items in stock.
    4. Once the stock details been added write some code to calculate how much it would cost to buy everything in stock.
"""
from random import randint

items = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

[print(f"The cost of {key} is ${value}.") for key, value in items.items()]
[items.update({key: {"cost": value, "stock": randint(0, 2)}}) for key, value in items.items()]

total = 0
for key, value in items.items():
    if value["stock"] == 0:
        print(f"{key.title()} sold out!")
        value["cost"] = 0
    total += value["cost"] * value["stock"]

print(f"The cost of everything in stock: {total}")


# TASK: Cars
"""
    1. Copy the following string into your code: "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".
    2. Convert it into a list using Python (don't do it by hand!).
    3. Print out a message saying how many manufacturers/companies are in the list.
    4. Print the list of manufacturers in reverse/descending order (Z-A).
    5. Using loops or list comprehension:
        1. Find out how many manufacturers' names have the letter 'o' in them.
        2. Find out how many manufacturers' names do not have the letter i' in them.
        
    6. Bonus: There are a few duplicates in this list:
        ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
        1. Remove these programmatically. (Hint: you can use sets to help you).
        2. Print out the companies without duplicates,
            in a comma-separated string with no line-breaks(eg. "Acura, Alfa Romeo, Aston Martin, .."),
            also print out a message saying how many companies are now in the list.

    7. Bonus:Print out the list of manufacturers in ascending order (A-Z),
        but reverse the letters of each manufacturer's name.
"""
companies = "Volkswagen, Toyota, Ford Motor, Honda, Chevrolet".split(", ")
print(f"There are {len(companies)} manufacturers/companies in the list.")
print(sorted(companies, reverse=True))

counter = []
[counter.append(company) for company in companies if company.count("o") > 0]
print(f"{len(counter)} companies have the letter 'o' in them")

counter.clear()
[counter.append(company) for company in companies if company.count("i") > 0]
print(f"{len(counter)} companies have the letter 'i' in them")

companies_list = ["Honda", "Volkswagen", "Toyota", "Ford Motor", "Honda", "Chevrolet", "Toyota"]
companies_set = set(companies_list)
print(", ".join(companies_set))
print(f"There are {len(companies_set)} companies in the list")

companies_list = sorted(list(companies_set))
print([company[::-1] for company in companies_list])
