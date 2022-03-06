# TASK: Formula
"""
    1. Write a program that calculates and prints a value according to this given formula:
    Q = Square root of [(2 * C * D) / H]
    2. Following are the fixed values of C and H:
        - C is 50.
        - H is 30.
    3. Ask the user for a comma-separated string of numbers,
        use each number from the user as D in the formula and return all the results For example,
        if the user inputs: 100, 150, 180 The output should be:
            >> 18,22,24
"""
import math
C = 50
H = 30
D_list = input("Enter D values comma-separated: ").split(",")
Q = []

for D in D_list:
    Q.append(round(math.sqrt((2 * C * int(D)) / H), 2))
print(Q, "\n")


# TASK: List of integers
"""
    Given a list of 10 integers to analyze. For example:
        [3, 47, 99, -80, 22, 97, 54, -23, 5, 7] 
        [44, 91, 8, 24, -6, 0, 56, 8, 100, 2] 
        [3, 21, 76, 53, 9, -82, -3, 49, 1, 76] 
        [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
        
    1. Store the list of numbers in a variable.
    2. Print the following information:
        a. The list of numbers - printed in a single line
        b. The list of numbers - sorted in descending order (largest to smallest)
        c. The sum of all the numbers
    3. A list containing the first and the last numbers.
    4. A list of all the numbers greater than 50.
    5. A list of all the numbers smaller than 10.
    6. A list of all the numbers squared - eg. for [1, 2, 3] you would print "[1, 4, 9]".
    7. The numbers without any duplicates - also print how many numbers are in the new list.
    8. The average of all the numbers.
    9. The largest number.
    10.The smallest number.
    11.Bonus: Find the sum, average, largest and smallest number without using built in functions.
    12.Extra bonus: Instead of using pre-defined lists of numbers, ask the user for 10 numbers between -100 and 100.
        - Ask the user for an integer between -100 and 100 - repeat this question 10 times.
        - Each number should be added into a variable that you created earlier.
"""
list_to_analyze = []
ordinal = ""
for i in range(1, 11):
    if i == 1: ordinal = "st"
    elif i == 2: ordinal = "nd"
    elif i == 3: ordinal = "rd"
    else: ordinal = "th"
    list_to_analyze.append(int(input(f"Enter a number between -100 and 100, {i}{ordinal} number: ")))

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


# TASK: Working on a paragraph
"""
    1. Find an interesting paragraph of text online. (Please keep it appropriate to the social context of our class.)
    2. Paste it to your code, and store it in a variable.
    3. Let's analyze the paragraph. Print out a nicely formatted message saying
    4. How many characters it contains (this one is easy..).
    5. How many sentences it contains.
    6. How many words it contains.
    7. How many unique words it contains.
    8. Bonus: How many non-whitespace characters it contains.
    9. Bonus: The average amount of words per sentence in the paragraph.
    10. Bonus: the amount of non-unique words in the paragraph.
"""
interesting = """
    Marie Curie was the first person to win two Nobel Prizes,
    and is one of only two people in the history of the Nobels to win in two different fields.
    She and her husband Pierre, along with Henri Becquerel,
    won the Physics Prize in 1903 for their discovery of radioactivity.
"""
words = interesting.split(' ')
sentences = interesting.count('.')

print(f"In this paragraph we have:\n"
      f"{len(interesting)} amount of characters\n"
      f"{sentences} amount of sentences\n"
      f"{len(words)} amount of words\n"
      f"{len(set(words))} amount of unique words\n"
      f"{len(interesting.replace(' ', ''))} amount of non-whitespace characters\n"
      f"{round(len(words) / sentences, 2)} average amount of words per sentence\n"
      f"{len(words) - len(set(words))} amount of non-unique words\n")


# TASK: Exercise 4
"""
    Write a program that prints the frequency of the words from the input.

    Suppose the following input is supplied to the program:
    New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.
    
    Then, the output should be:

    >> 2:2
    >> 3.:1
    >> 3?:1
    >> New:1
    >> Python:5
    >> Read:1
    >> and:1
    >> between:1
    >> choosing:1
    >> or:2
    >> to:1
"""
some_string = "New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

for string in set(some_string.split(" ")):
    print(f"{string}: {some_string.count(string)}")
