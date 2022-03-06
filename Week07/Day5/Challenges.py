import math
from functools import reduce


# TASK: Exercise 1
def insert_letter(some_list, index, item):
    """
        Write a script that inserts an item at a defined index in a list.
    """
    some_list.insert(index, item)
    print("Exercise 1:", some_list)


insert_letter([1, 2, 3, 4], 2, "g")


# TASK: Exercise 2
def count_spaces(string):
    """
        Write a script that counts the number of spaces in a string.
    """
    print("Exercise 2:", string.count(" "))


count_spaces("what a strange string to send as an argument")


# TASK: Exercise 3
def count_upper_and_lower(string):
    """
        Write a script that calculates the number of upper case letters and lower case letters in a string.
    """
    print("Exercise 3.1:", len([letter for letter in string if letter.isupper()]))
    print("Exercise 3.2:", len([letter for letter in string if letter.islower()]))


count_upper_and_lower("What a Strange string To send As An argument")


# TASK: Exercise 4
def my_sum(some_list):
    """
        Write a function to find the sum of an array without using the built-in function:

        >> my_sum([1,5,4,2])
        >> 12
    """
    print("Exercise 4:", reduce(lambda a, b: a + b, some_list))


my_sum([1, 5, 4, 2])


# TASK: Exercise 5
def find_max(some_list):
    """
        Write a function to find the max number in a list

        >> find_max([0,1,3,50])
        >> 50
    """
    print("Exercise 5:", max(some_list))


find_max([0, 1, 3, 50])


# TASK: Exercise 6
def factorial(num):
    """
        Write a function that returns factorial of a number

        >> factorial(4)
        >> 24
    """
    print("Exercise 6:", reduce(lambda a, b: a * b, list(range(1, num + 1))))


factorial(4)


# TASK: Exercise 7
def list_count(some_list, item):
    """
        Write a function that counts an element in a list (without using the count method):

        >> list_count(['a','a','t','o'],'a')
        >> 2
    """
    print("Exercise 7:", some_list.count(item))


list_count(['a', 'a', 't', 'o'], 'a')


# TASK: Exercise 8
def norm(some_list):
    """
        Write a function that returns the L2-norm (square root of the sum of squares) of the sum of a list:

        >> norm([1,2,2])
        >> 3
    """
    print("Exercise 8:", math.sqrt(sum(map(lambda a: a ** 2, some_list))))


norm([1, 2, 2])


# TASK: Exercise 9
def is_mono(some_list):
    """
        Write a function to find if an array is monotonic (sorted either ascending of descending)

        >> is_mono([7,6,5,5,2,0])
        >> True

        >> is_mono([2,3,3,3])
        >> True

        >> is_mono([1,2,0,4])
        >> False
    """
    print("Exercise 9:", some_list == sorted(some_list) or some_list == sorted(some_list, reverse=True))


is_mono([7, 6, 5, 5, 2, 0])
is_mono([2, 3, 3, 3])
is_mono([1, 2, 0, 4])


# TASK: Exercise 10
def longest_word(some_list):
    """
        Write a function that prints the longest word in a list.
    """
    length_list = list(map(lambda a: len(a), some_list))
    print("Exercise 10:", some_list[length_list.index(max(length_list))])


longest_word(["What", "a", "ridiculous", "string", "To", "send", "As", "An", "argument"])


# TASK: Exercise 11
def sort_types(some_list):
    """
        Given a list of integers and strings, put all the integers in one list, and all the strings in another one.
    """
    integer_list = [item for item in some_list if type(item) is int]
    string_list = [item for item in some_list if type(item) is str]
    print("Exercise 11:", integer_list, string_list)


sort_types(["What", 7, 5, "string", "To", "send", 2, "An", 1])


# TASK: Exercise 12
def is_palindrome(some_string):
    """
        Write a function to check if a string is a palindrome:

        >> is_palindrome('radar')
        >> True

        >> is_palindrome('John')
        >> False
    """
    if some_string == some_string[::-1]:
        print("Exercise 12:", True)
    else:
        print("Exercise 12:", False)


is_palindrome('radar')
is_palindrome('John')


# TASK: Exercise 13
def sum_over_k(some_string, k):
    """
        Write a function that returns the amount of words in a sentence with length > k:

        >> sentence = 'Do or do not there is no try'
        >> k=2
        >> sum_over_k(sentence,k)
        >> 3
    """
    print("Exercise 13:", sum([True for item in some_string.split(' ') if len(item) > k]))


sum_over_k('Do or do not there is no try', 2)


# TASK: Exercise 14
def dict_avg(some_dict):
    """
        Write a function that returns the average value in a dictionary (assume the values are numeric):

        >> dict_avg({'a': 1, 'b': 2, 'c': 8, 'd': 1})
        >> 3
    """
    avg = sum(some_dict.values()) / len(some_dict.values())
    print("Exercise 14:", avg)
    return avg


dict_avg({'a': 1, 'b': 2, 'c': 8, 'd': 1})


# TASK: Exercise 15
def common_div(first_num, second_num):
    """
        Write a function that returns common divisors of 2 numbers:

        >> common_div(10,20)
        >> [2,5,10]
    """
    common_divs = [num for num in range(2, max(first_num, second_num))
                   if first_num % num == 0 and second_num % num == 0]
    print("Exercise 15:", common_divs)
    return common_divs


common_div(10, 20)


# TASK: Exercise 16
def is_prime(some_num):
    """
        Write a function that test if a number is prime:

        >> is_prime(11)
        >> True
    """
    print("Exercise 16:", sum([True for num in range(2, some_num) if some_num % num == 0]) == 0)


is_prime(11)


# TASK: Exercise 17
def weird_print(some_list):
    """
        Write a function that prints elements of a list if the index and the value are even:

        >> weird_print([1, 2, 2, 3, 4, 5])
        >> [2, 4]
    """
    print("Exercise 17:", [num for i, num in enumerate(some_list) if i % 2 == 0 and num % 2 == 0])


weird_print([1, 2, 2, 3, 4, 5])


# TASK: Exercise 18
def type_count(**kargs):
    """
        Write a function that accepts an undefined number of keyword arguments and return the count of different types:

        >> type_count(a=1,b='string',c=1.0,d=True,e=False)
        >> int: 1, str:1 , float:1, bool:2
    """
    types = {type(item).__name__: 0 for item in kargs.values()}
    [types.update({item_type: types[item_type] + 1}) for item_type in types.keys() for item in kargs.values()
     if type(item).__name__ == item_type]
    print("Exercise 18:", types)


type_count(a=1, b='string', c=1.0, d=True, e=False)


# TASK: Exercise 19
def homemade_split(some_string, splitter):
    """
        Write a function that mimics the builtin .split() method for strings.
        By default, the function uses whitespace,
        but it should be able to take an argument for any character and split with that argument.
    """
    splinted_list = []
    while len(some_string):
        if some_string.count(splitter) > 0:
            index = some_string.index(splitter)
            splinted_list.append(some_string[0: index])
            some_string = some_string[index+1: len(some_string)]

        else:
            splinted_list.append(some_string[0: len(some_string)])
            some_string = ""

    print("Exercise 19:", splinted_list)


homemade_split("what a strange string to send as an argument", " ")


# TASK: Exercise 20
def weird_print(some_string):
    """
        Convert a string into password format.

        Example:
            input : "mypassword"
            output: "***********"
    """
    print("Exercise 20:", len(some_string) * "*")


weird_print("mypassword")
