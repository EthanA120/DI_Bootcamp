# TASK: Anagram checker
from anagram_checker import AnagramChecker


def anagrams():
    """
        We will create a program that will ask the user for a word.
        It will check if the word is a valid English word, and then find all possible anagrams for that word.

        Instructions
        First Download this text file: https://norvig.com/ngrams/sowpods.txt

        1. Create a new file called anagram_checker.py which contains a class called AnagramChecker.

        2. The class should have the following methods:
            - __init__ - should load the word list file (text file) into a variable, so that it can be searched later on in the code.

            - is_valid_word(word) – should check if the given word (i.e. the word of the user) is a valid word.

            - get_anagrams(word) – should find all anagrams for the given word. (eg. if word of the user is ‘meat’, the function should return a list containing [“mate”, “tame”, “team”].)

            - Hint: you might want to create a separate method called is_anagram(word1, word2), that will compare 2 words and return True if they contain the same letters (but not in the same order), and False if not.

            Note: None of the methods in the class should print anything.

        3. Now create another Python file, called anagrams.py. This will contain all the UI (user interface) functionality of your program, and will rely on AnagramChecker for the anagram-related logic.

        4. It should do the following:
            1. Show a menu, offering the user to input a word or exit. Keep showing the menu until the user chooses to exit.

            2. If the user chooses to input a word, it must be accepted from the user’s keyboard input, and then be validated:
                - Only a single word is allowed. If the user typed more than one word, show an error message. (Hint: how do we know how many words were typed?)
                - Only alphabetic characters are allowed. No numbers or special characters.
                - Whitespace should be removed from the start and end of the user’s input.

            3. Once your code has decided that the user’s input is valid, it should find out the following:
                - All possible anagrams to the user’s word.
                - Create an AnagramChecker instance and apply it to the steps created above.
                - Display the information about the word in a user-friendly, nicely-formatted message such as:


                YOUR WORD :”MEAT”
                this is a valid English word.
                Anagrams for your word: mate, tame, team.
    """
    user_input = ""
    word = ""
    while user_input not in ["E", "Q", "e", "q"]:
        user_input = input(
            "Menu:\n"
            "(W)ord select\n"
            "(S)ummary\n"
            "(C)heck word\n"
            "(G)et anagrams\n"
            "(A)nagram check\n"
            "(Q)uit\n"
            "Choice: "
        ).upper()

        if user_input not in ("W", "C", "G", "A", "Q"):
            print("Error! Not a valid option")
        print()

        try:
            match user_input:
                case "W":
                    user_word = input("Enter your word: ")
                    if user_word.isalpha():
                        word = AnagramChecker(user_word)
                    else:
                        raise ValueError

                case "S":
                    if word.is_valid_word():
                        valid = "is a valid"
                    else:
                        valid = "isn't a valid"
                    print(f'Your word is: "{word.word}"\n'
                          f'This {valid} English word.\n'
                          f'Anagrams for your word: {", ".join(word.get_anagrams())}\n')

                case "C":
                    print(word.is_valid_word(), "\n")

                case "G":
                    print(word.get_anagrams(), "\n")

                case "A":
                    print(word.is_anagram(word.word, input("Enter second word: ")), "\n")
        except AttributeError:
            print("Error! Choose a word first!\n")
        except ValueError:
            print("Error! Word can only contain english characters!\n")


anagrams()
