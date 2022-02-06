# TASK: List of Integers - Randoms
"""
    Continuation of the Exercise 2 XP NINJA from Week6Day4

    1. Instead of asking the user for 10 integers, generate 10 random integers yourself.
        Make sure that these random integers are between -100 and 100.

    2. Instead of always generating 10 integers, let the amount of integers also be random!
        Generate a random positive integer no smaller than 50.

    3. Will the code work when the number of random numbers is not equal to 10?
"""
from random import randint

list_to_analyze = [randint(-100, 100) for num in range(randint(50, 100))]

greater_than_50 = []
smaller_than_10 = []
squared_list = []
sum_of_nums = 0
amount_of_nums = 0
maximum = 0
minimum = 0
for num in list_to_analyze:
    if num > 50:
        greater_than_50.append(num)
    elif num < 10:
        smaller_than_10.append(num)

    squared_list.append(num**2)

    sum_of_nums += num
    amount_of_nums += 1
    if maximum < num:
        maximum = num

    if minimum > num:
        minimum = num

print(list_to_analyze)
print(sorted(list_to_analyze, reverse=True))
print(f"Sum with built in function: {sum(list_to_analyze)}, without: {sum_of_nums}")
print([list_to_analyze[0], list_to_analyze[-1]])
print(greater_than_50)
print(smaller_than_10)
print(squared_list)
without_duplicates = list(set(list_to_analyze))
print(without_duplicates, len(without_duplicates))
print(f"Average with: {sum(list_to_analyze) / len(list_to_analyze)}, without: {sum_of_nums / amount_of_nums}")
print(f"Max with: {max(list_to_analyze)}, without: {maximum}, Min with: {min(list_to_analyze)}, without: {minimum}\n")


# TASK: Authentication CLI - login, TASK: Authentication CLI - signup
"""
    1. Create a dictionary that contains users: each key will represent a username,
        and each value will represent that user's password. Initialize this dictionary with 3 users &passwords.
        
    2. Create a loop that does the following:
        1. If the user inputs "exit", break out of the loop.
        2. If the user inputs "login", ask them for their username and password.
            1. If the user's details exist print "you are now logged in".
            2. If the user is successfully logged in,
                store the username in a variable called logged_in so we can track it later.
                
    3. Authentication CLI - signup:
        Continuation of the Exercise Above - Authentication CLI - login

        1. If the user does not exist ask if they would like to sign up:
            1. Ask the user for a username and make sure it doesn't exist as a key in our dictionary,
                if the username is not valid continue asking the user to input a username.
            2. Ask the user for a password. The password is the value.
"""
users_dict = {"athos": 123, "porthos": 456, "aramis": 789}

flag = True
while flag:
    user_input = input("What do you want to do?\n").lower()
    if user_input == "exit":
        print("Good bye")
        flag = False

    elif user_input == "login":
        username = input("Enter username: ").lower()
        if username in users_dict.keys():
            password = input("Enter password: ")

            if int(password) == users_dict[username]:
                print("You are now logged in")
                logged_in = username
                flag = False
            else:
                print("Wrong password")
        
        else:
            check = ["y", "yes", "n", "no"]
            sign_up = input("No such username, would you like to sign up? Y/N").lower()
            while sign_up not in check:
                sign_up = input("Only 'Y' or 'N' are valid, would you like to sign up?").lower()

            if sign_up in ["y", "yes"]:
                new_user = input("Choose username: ").lower()
                while new_user in users_dict.keys():
                    print("User already exist.")
                    new_user = input("Choose different username: ").lower()
                new_password = int(input("Choose password: "))
                users_dict[new_user] = new_password
                print(users_dict)

            else:
                print("Good bye")
                flag = False
