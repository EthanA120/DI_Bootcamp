# TASK: Favorite numbers
"""
    1. Create a set called my_fav_numbers with all your favorites numbers.
    2. Add two new numbers to the set.
    3. Remove the last number.
    4. Create a set called friend_fav_numbers with your friend's favorites numbers.
    5. Concatenate my_fav_numbers and friend_fav_numbers to a new variable called Our_fav_numbers.
"""
my_fav_numbers = {0, 1}
my_fav_numbers.update([3.14, 2.72])
my_fav_numbers.discard(max(my_fav_numbers))
friend_fav_numbers = [-1, 9.81]
Our_fav_numbers = my_fav_numbers.union(friend_fav_numbers)
print(Our_fav_numbers, "\n")


# TASK: Tuple
"""
    Given a tuple which value is integers, is it possible to add more integers to the tuple?
"""
# Yes
some_tuple = (0, 1, 2)

# Add one element:
some_tuple += tuple([4])
print(some_tuple)

# Add several elements:
some_tuple += (4, 5, 6)
print(some_tuple, "\n")


# TASK: Print a range of numbers
"""
    Use a for loop to print all numbers from 1 to 20, inclusive.
"""
for num in range(1, 21):
    print(num)
print()


# TASK: Floats
"""
    1. Recap- What is a float? What is the difference between an integer and a float?
    2. Can you think of another way to generate a sequence of floats?
    3. Create a list containing the following sequence 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5 (don't hard-code the sequence).
"""
# 1. integer is a natural number (1, 2, 3...), float is a number with a floating point (decimal number: 1.25, 5.213...)
# another way from what other way?

for num in range(3, 11):
    if num % 2 == 0:
        print(int(num / 2))
    else:
        print(num / 2)
print()


# TASK: Shopping List
"""
    Using this list basket = ["Banana", "Apples", "Oranges ", "Blueberries "]
    1. Remove "Banana" from the list.
    2. Remove "Blueberries" from the list.
    3. Add "Kiwi" to the end of the list.
    4. Add "Apples" to the beginning of the list.
    5. Count how many apples are in the basket.
    6. Empty the basket.
    7. Print(basket)
"""
basket = ["Banana", "Apples", "Oranges", "Blueberries"]

basket.remove("Banana")
basket.remove("Blueberries")
basket.append("Kiwi")
basket.insert(1, "Apples")
print(basket.count("Apples"))
basket.clear()
print(basket, "\n")


# TASK: Loop
"""
    Write a while loop that will continuously ask the user for their name, unless the input is equal to your name.
"""
name = ""
while name != "Ethan":
    name = input("Enter my name: ")
print()


# TASK: Exercise 7
"""
    Given a list, use a loop to print out every element which has an even index.
"""
for i, num in enumerate(range(1, 21)):
    if i % 2 == 0:
        print(i, ":", num)


# TASK: Exercise 8
"""
    Create a loop that goes from 1500 to 2500 and prints all multiples of 5 and 7.
"""
for num in range(1500, 2500):
    if num % 5 == 0 and num % 7 == 0:
        print(num)
print()


# TASK: Favorite fruits
"""
    1. Ask the user to input their favorite fruit(s) (one or several fruits).
        Hint: Use the built in input method.
        Ask the user to separate the fruits with a single space, eg. "apple mango cherry".
        
    2. Store the favorite fruit(s) in a list (convert the string of words into a list of words).
    
    3. Now that we have a list of fruits, ask the user to input a name of any fruit.
        - If the user's input is in the favorite fruits list, print "You chose one of your favorite fruits! Enjoy!".
        - If the user's input is NOT in the list, print, "You chose a new fruit. I hope you enjoy".
"""
user_favorite_fruits = input("Enter your favorite fruits (seperated with single space): ")

favorite_fruits_list = user_favorite_fruits.split(" ")

extra_fruit = input("Enter a fruit")
if extra_fruit in favorite_fruits_list:
    print("You chose one of your favorite fruits! Enjoy!", "\n")
else:
    print("You chose a new fruit. I hope you enjoy", "\n")


# TASK: Who ordered a pizza?
"""
    1. Write a loop that asks a user to enter a series of pizza toppings,
        when the user inputs 'quit' stop asking for toppings.
        
    2. As they enter each topping, print a message saying you'll add that topping to their pizza.
    
    3. Upon exiting the loop print all the toppings on the pizza pie and what the total price is
        10+2.5 for each topping.
"""
user_topping = ""
toppings = []

while user_topping != "quit":
    user_topping = input("Enter a topping (or type 'quit' to end the program): ")
    # if user_topping != "quit":
    print(f"You'll add a {user_topping} to the pizza")
    toppings.append(user_topping)

print(f"{', '.join(toppings)}: ${10 + len(toppings) * 2.5}\n")


# TASK: Cinemax
"""
    1. A movie theater charges different ticket prices depending on a person's age.
        - if a person is under the age of 3, the ticket is free.
        - if they are between 3 and 12, the ticket is $10.
        - if they are over the age of 12, the ticket is $15.
    
    2. Ask a family the age of each person who wants a ticket.
    
    3. Store the total cost of all the family's tickets and print it out.
    
    4. A group of teenagers are coming to your movie theater,
        they want to watch a movie that is restricted for people between the ages of 16 and 21.
        Write a program that asks every user for their age,
        and prints a list of the teens who are permitted to watch the movie.
"""
age_list = input("Enter the ages seperated with space: ").split(" ")
total = 0

for age in age_list:
    age = int(age)
    if age < 3:
        continue
    elif 3 <= age < 12:
        total += 10
    else:
        total += 15
print(total, "\n")

teens = {}
teens_input = input("Enter the name and age seperated with comma ',' and separate every teen with space:\n").split(" ")
for teen in teens_input:
    teen = teen.split(",")
    teens[teen[0]] = int(teen[1])

permitted = []
for teen in teens.keys():
    if 16 < teens[teen] < 21:
        permitted.append(teen)

print(permitted)


# TASK: Who is under 16?
"""
    1. Given a list of names, write a program that asks every user for their age,
        if they are less than 16 years old remove them from the list.
    2. At the end, print the final list.
"""
name_list = ["Ethan", "Moshe", "Jacob", "Jordan", "Adir", "Ravid"]

for name in name_list.copy():
    user_age = int(input(f"{name}, enter your age: "))
    if user_age < 16:
        name_list.remove(name)

print(name_list)


# TASK: Exercise 13
"""
    1. Make a list called sandwich_orders and fill it with the names of various sandwiches.
    2. Then make an empty list called finished_sandwiches.
    3. As each sandwich is made, move it to the list of finished sandwiches.
    4. After all the sandwiches have been made,
        print a message listing each sandwich that was made, such as "I made your tuna sandwich".
"""
sandwich_orders = ["Tuna", "Omlet", "Avocado", "Salmon"]
finished_sandwiches = []

for sandwich in sandwich_orders:
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich} sandwich")
print()


# TASK: Exercise 14
"""
    1. Using the list sandwich_orders from Exercise 13,
        make sure the sandwich 'pastrami' appears in the list at least three times.
        
    2. Add code near the beginning of your program to print a message saying the deli has run out of pastrami,
        and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.
    
    3. Make sure no pastrami sandwiches end up in finished_sandwiches.
"""
for i in range(3):
    sandwich_orders.append("pastrami")

print("We are sorry to announce that the deli has run out of pastrami")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

print(sandwich_orders)
