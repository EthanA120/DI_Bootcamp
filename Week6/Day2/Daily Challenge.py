# TASK: Build up a string
"""
    1. Using the input function, ask the user for a string. The string must be 10 characters long.
        - If it’s less than 10 characters, print a message which states “string not long enough”.
        - If it’s more than 10 characters, print a message which states “string too long”.

    2. Then, print the first and last characters of the given text.

    3. Construct the string character by character: Print the first character,
    then the second, then the third, until the full string is printed. For example:

    The user enters "Hello World"
    Then, you have to construct the string character by character:
    >>> 'H'
    >>> 'He'
    >>> 'Hel'
    >>> '... etc'
    >>> 'Hello World'
"""
user_input = input("Enter some text (exact 10 char long): ")
top = 10

if len(user_input) < top:
    print("string not long enough")
elif len(user_input) > top:
    print("string too long")

print("first: ", user_input[0], " last: ", user_input[-1])

for i in range(len(user_input) + 1):
    print(user_input[0:i])
