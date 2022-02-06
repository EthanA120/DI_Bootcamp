# TASK: Convert lists into dictionaries
"""
    Convert the two following lists, into dictionaries.
    Hint: Use the zip method

    keys = ['Ten', 'Twenty', 'Thirty']
    values = [10, 20, 30]

    Expected output:
    >> {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
"""
keys_list = ['Ten', 'Twenty', 'Thirty']
values_list = [10, 20, 30]
print(dict(zip(keys_list, values_list)), "\n")


# TASK: Cinemax #2
"""
    "Continuation of Exercise Cinemax from Week6Day4 XP"
    1. A movie theater charges different ticket prices depending on a person's age.
        - if a person is under the age of 3, the ticket is free.
        - if they are between 3 and 12, the ticket is $10.
        - if they are over the age of 12, the ticket is $15.
        
    2. Given the following object:
        family = {'rick': 43, 'beth': 13, 'morty': 5, 'summer': 8}
        
    3. How much does each family member have to pay?
    
    4. Print out the family's total cost for the movies.
    
    5. Bonus: Ask the user to input the names and ages instead of using the provided family variable
        Hint: ask the user for names and ages and add them into a family dictionary that is initially empty.
"""
age_list = input("Enter the name and age seperated with comma ',' and separate every costumer with space:\n").split(" ")
age_dict = {}
total = 0
to_display = []

for costumer in age_list:
    costumer_list = costumer.split(",")
    age_dict[costumer_list[0]] = int(costumer_list[1])

for name, age in age_dict.items():
    age_dict[name] = [age]

    if age < 3:
        age_dict[name].append(0)

    elif 3 <= age < 12:
        age_dict[name].append(10)
        total += 10

    else:
        age_dict[name].append(15)
        total += 15

    to_display += []

print([f"{name}: {age_dict[name][1]}" for name in age_dict.keys()])
print("total:", total, "\n")


# TASK: Zara
"""
    1. Here is some information about a brand:
        name: Zara 
        creation_date: 1975 
        creator_name: Amancio Ortega Gaona 
        type_of_clothes: men, women, children, home 
        international_competitors: Gap, H&M, Benetton 
        number_stores: 7000 
        major_color: 
            France: blue, 
            Spain: red, 
            US: pink, green
    2. Create a dictionary called brand which value is the information from part one (turn the info to keys and values).
    3. Change the number of stores to 2.
    4. Print a sentence that explains who Zaras clients are.
    5. Add a key called country_creation with a value of Spain.
    6. Check if the key international_competitors is in the dictionary. If it is, add the store Desigual.
    7. Delete the information about the date of creation.
    8. Print the last international competitor.
    9. Print the major clothes colors in the US.
    10. Print the amount of key value pairs (ie. length of the dictionary).
    11. Print the keys of the dictionary.
    12. Create another dictionary called more_on_zara with the following details:
        creation_date : 1975
        number_stores : 10000
    13. Use a method to add the information from the dictionary more_on_zara to the dictionary brand.
    14. Print the value of the key number_stores. What just happened ?
"""
brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2

print(f"{brand['name']} provides cloths types that suits for {', '.join(brand['type_of_clothes'])}")

brand["country_creation"] = "Spain"

brand["international_competitors"].append("Desigual") if "international_competitors" in brand else print("No such key!")

brand.pop("creation_date")

print(brand["international_competitors"][-1])

print(", ".join(brand["major_color"]["US"]))

print(len(brand))

print(", ".join(brand.keys()), "\n")

brand.update({"more_on_zara": {"creation_date": 1975, "number_stores": 10000}})

# print(brand[5]) No such thing


# TASK: Disney characters
"""
    Use this list :
        users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
    
    Analyse these results :
    #1/
        >>> print(disney_users_A)
        {"Mickey": 0, "Minnie": 1, "Donald": 2, "Ariel": 3, "Pluto": 4}

    #2/
        >>> print(disney_users_B)
        {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
    
    #3/
        >>> print(disney_users_C)
        {"Ariel": 0, "Donald": 1, "Mickey": 2, "Minnie": 3, "Pluto": 4}
        
    1. Use a for loop to recreate the 1st result. Tip: don't hardcode the numbers.
    2. Use a for loop to recreate the 2nd result. Tip: don't hardcode the numbers.
    3. Use a method to recreate the 3rd result. Hint: The 3rd result is sorted alphabetically.
    4. Only recreate the 1st result for:
        1. The characters, which names contain the letter "i".
        2. The characters, which names start with the letter "m" or "p".
"""
users = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]

disney_users_A = {}
disney_users_B = {}
disney_users_C = {}
disney_users_D = {}
disney_users_E = {}
D = 0
E = 0

for i, user in enumerate(users):
    disney_users_A[user] = i
    disney_users_B[i] = user

    if "i" in user:
        disney_users_D[user] = D
        D += 1

    if user.lower().startswith(("m", "p")):
        disney_users_E[user] = E
        E += 1

for i, user in enumerate(sorted(users)):
    disney_users_C.update({user: i})

print(disney_users_A)
print(disney_users_B)
print(disney_users_C)
print(disney_users_D)
print(disney_users_E)
