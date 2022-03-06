# TASK: What’s your name?
"""
    1. Write a function called get_full_name() that takes three arguments:
        1: first_name
        2: middle_name
        3: last_name
    2. middle_name should be optional, if it’s omitted by the user,
        the name returned should only contain the first and the last name.

    For example, get_full_name(first_name="john", middle_name="hooker", last_name="lee") will return John Hooker Lee.
    But get_full_name(first_name="bruce", last_name="lee") will return Bruce Lee.
"""
def get_full_name(first_name, last_name, middle_name=""):
    return f"{first_name} {middle_name} {last_name}"


name = input("What is your name? ").split(" ")
if len(name) == 2:
    print(get_full_name(name[0], name[1]))
elif len(name) > 2:
    print(get_full_name(name[0], name[-1], name[1]))


# TASK: From English to Morse
"""
    Write a function that converts English text to morse code and another one that does the opposite.
    
    Hint: Check the internet for a translation table,
        every letter is separated with a space and every word is separated with a slash /.
"""
MORSE = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ', ': '--..--',
    '.': '.-.-.-',
    '?': '..--..',
    '/': '-..-.',
    '-': '-....-',
    '(': '-.--.',
    ')': '-.--.-'
}


def code_encrypt(string):
    code = ""

    for letter in string:
        if letter.upper() != " " and letter in MORSE.keys():
            code += MORSE[letter] + " "
        else:
            code = code[0:-1] + "/"

    print(code)

def code_decrypt(code):
    string = ""
    code_list = code.split("/")

    for word in code_list:
        letters = word.split(" ")
        for letter in letters:
            if letter in MORSE.values():
                word_key = list(MORSE.keys())[list(MORSE.values()).index(letter)]
                string += word_key
        string += " "

    print(string[0:-1])


code_decrypt("--. . . -.- .../..-. --- .-./--. . . -.- ...")
code_encrypt("GEEKS FOR GEEKS")
