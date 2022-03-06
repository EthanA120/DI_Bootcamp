# TASK: Hello World
"""
   Print the following output in one line of code:

   >>> "Hello world"
   >>> "Hello world"
   >>> "Hello world"
   >>> "Hello world"
"""
print("Hello world\nHello world\nHello world\nHello world\n")


# TASK: Some Math
"""
    Write code that calculates the result of:
        (99^3) * 8 (99 to the power of 3 times 8)
"""
print((99 ** 3) * 8, "\n")


# TASK: What is the output ?
"""  
    Predict the output of the following code snippets:

    >>> 5 < 3
    >>> 3 == 3
    >>> 3 == "3"
    >>> "3" > 3
    >>> "Hello" == "hello"
"""
# 5 < 3               : False
# 3 == 3              : True
# 3 == "3"            : False
# "3" > 3             : False
# "Hello" == "hello"  : False


# TASK: Your computer brand
"""
    1. Create a variable called computer_brand which value is the brand name of your computer.
    2. Using the computer_brand variable print a sentence that states the following:
        "I have a <computer_brand> computer".
"""
computer_brand = "Assus"
print(f"I have a {computer_brand} computer\n")


# TASK: Your information
"""
    1. Create a variable called name, and set it's value to your name.
    2. Create a variable called age, and set it's value to your age.
    3. Create a variable called shoe_size, and set it's value to your shoe size.
    4. Create a variable called info and set it's value to an interesting sentence about yourself.
        The sentence must contain all the variables created in parts 1, 2 and 3.
    5. Have your code print the info message.
    6. Run your code
"""
name = "Ethan"
age = 28
shoe_size = 42
info = f"My name is {name}, I'm {age} years old and my shoe size is {shoe_size}\n"
print(info)


# TASK: A & B
"""
    1. Create two variables, a and b.
    2. Each variables value should be a number.
    3. If a is bigger then b, have your code print Hello World.
"""
a, b = 3, 2

if a > b:
    print("Hello World")


# TASK: Odd or Even
"""
    Write code that asks the user for a number and determines whether this number is odd or even.
"""
user_input = int(input("Enter a number"))

if user_input % 2 == 0:
    print("The number is even!")
else:
    print("NUmber is odd!")


# TASK: What's your name ?
"""
    Write code that asks the user for their name and determines whether or not you have the same name,
    print out a funny message based on the outcome.
"""
user1_name = input("Enter name #1: ")
user2_name = input("Enter name #2: ")
print(f"{user1_name} told {user2_name} knok knok jokes until {user2_name} knoked down")


# TASK: Tall enough to ride a roller coaster
"""
    1. Write code that will ask the user for their height in inches.
    2. If they are over 145cm print a message that states they are tall enough to ride.
    3. If they are not tall enough print a message that says they need to grow some more to ride.
"""
height_in = int(input("Enter your height in inches: "))

if height_in * 2.54 > 145:
    print("You are tall enough to ride!")
else:
    print("You can't ride, You are NOT tall enough!")
