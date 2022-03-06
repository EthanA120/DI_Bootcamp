# TASK: Concatenate lists
"""
    Write code that concatenates two lists together without using the + sign.
"""
list1 = [0, 1, 2]
list2 = [3, 4, 5]
united_list = list1.copy()

for item in list2:
    united_list.append(item)
print(united_list, "\n")


# TASK: Greatest Number
"""
    Ask the user for 3 numbers and print the greatest number.
    
    >> Input the 1st number: 25
    >> Input the 2nd number: 78
    >> Input the 3rd number: 87

    >> The greatest number is: 87
"""
count = ["1st", "2nd", "3rd"]
greatest = 0

for ith in count:
    user_number = int(input(f"Enter the {ith} number: "))
    if greatest < user_number:
        greatest = user_number

print(f"The greatest number is: {greatest}\n")


# TASK: The Alphabet
"""
    1. Create a string of all the letters in the alphabet
    2. Loop over each letter and print a message that contains the letter and whether its a vowel or a consonant.
"""
alphabet = ""
for num in range(65, 91):
    alphabet += chr(num)

for letter in alphabet:
    if letter in ["A", "E", "I", "O", "U"]:
        print(f"{letter} is vowel")
    else:
        print(f"{letter} is consonant")


# TASK: Exercise 4
"""
    names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']

    Ask a user for their name,
        if their name is in the names list print out the index of the first occurence of the name.

    Example: if input is 'Cortana' we should be printing the index 1
"""
names = ['Samus', 'Cortana', 'V', 'Link', 'Mario', 'Cortana', 'Samus']
user_name = input("Enter a name: ")

if user_name in names:
    print(names.index(user_name))


# TASK: Words and letters
"""
    1. Ask a user for 7 words, store them in a list named words.
    2. Ask the user for a single character, store it in a variable called letter.
    3. Loop through the words list and print the index of the first appearance of the letter in each word of the list.
    4. If the letter doesn't exist in one of the words, print a friendly message with the word and the letter.
"""
words = input("Enter 7 words seperated with space: ").split(" ")
letter = input("Enter a letter: ").lower()

indices = []
for word in words:
    word = word.lower()
    if letter in word:
        indices.append(word.index(letter))
    else:
        print(f"The letter is not exist in the word {word}")

print(indices, "\n")


# TASK: Exercise 6
"""
    Create a list of numbers from one to one million,
    then use min() and max() to make sure your list actually starts at one and ends at one million.
    Use the sum() function to see how quickly Python can add a million numbers.
"""
mega_list = list(range(1, 10 ** 6))
print(min(mega_list), max(mega_list), sum(mega_list), "\n")


# TASK: Exercise 7
"""
    Write a program which accepts a sequence of comma-separated numbers.
    Generate a list and a tuple which contain every number.

    Suppose the following input is supplied to the program: 34,67,55,33,12,98
    
    Then, the output should be:
    
    >> ['34', '67', '55', '33', '12', '98']
    >> ('34', '67', '55', '33', '12', '98')
"""
user_numbers = input("Enter some numbers seperated with comma ',': ").split(",")

user_numbers_list = []
for num in user_numbers:
    user_numbers_list.append(int(num))

user_numbers_tuple = tuple(user_numbers_list)
print(f"{user_numbers_list}\n{user_numbers_tuple}\n")


# TASK: Random number
"""
    1. Ask the user to input a number from 1 to 9 (including).
    2. Get a random number between 1 and 9. Hint: random module.
    3. If the user guesses the correct number print a message that says Winner.
    4. If the user guesses the wrong number print a message that says better luck next time.
    5. Bonus: use a loop that allows the user to keep guessing until they want to quit.
    6. Bonus 2: on exiting the loop tally up and display total games won and lost.
"""
from random import randint

user_num = 1
wins = 0
loses = 0
total_games = 0

rand_num = randint(1, 9)
while user_num != 0:
    user_num = int(input("Enter a number from 1 to 9 including: "))

    if user_num != 0:
        total_games += 1
        if user_num == rand_num:
            print("Winner!")
            wins += 1
        else:
            print("Better luck next time")
            loses += 1

if total_games != 0:
    print(f"Total games: {total_games}, Won: {wins}, Lose: {loses}, Win ratio: {wins / total_games}")
else:
    print("No games played")
print(1/90)
