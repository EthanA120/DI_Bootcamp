# TASK: Hangman
"""
    - The computer choose a random word and mark stars for each letter of each word.
    - Then the player will guess a letter.
        - If that letter is in the word(s) then the computer fills the letter in all the correct positions of the word.
        - If the letter isn’t in the word(s) then add a body part to the gallows
            (head, body, left arm, right arm, left leg, right leg).
        - The player will continue guessing letters until they can either solve the word(s) (or phrase)
            or all six body parts are on the gallows.
        - The player can’t guess the same letter twice.

    Here is a piece of code that will give you a random word:
    import random

    words_list = ['correction', 'childish', 'beach', 'python', 'assertive', 'interference', 'complete', 'share', 'credit card', 'rush', 'south']
    word = random.choice(wordslist)
"""
from random import choice


def pics(num):
    """
        returns one of the hangman pictures
        :param num: wanted picture number
        :type num: int
        :return: ascii art of matching picture
        :rtype: string
    """

    if num == 0:
        return '''
            x-------x
        '''

    if num == 1:
        return '''
            x-------x
            |
            |
            |
            |
            |
        '''

    if num == 2:
        return '''
            x-------x
            |       |
            |       0
            |
            |
            |
        '''

    if num == 3:
        return '''
            x-------x
            |       |
            |       0
            |       |
            |
            |
        '''

    if num == 4:
        return '''
            x-------x
            |       |
            |       0
            |      /|\\
            |
            |
        '''

    if num == 5:
        return '''
            x-------x
            |       |
            |       0
            |      /|\\
            |      /
            |
        '''

    if num == 6:
        return '''
            x-------x
            |       |
            |       0
            |      /|\\
            |      / \\
            |
        '''


words_list = [
    'correction',
    'childish',
    'beach',
    'python',
    'assertive',
    'interference',
    'complete',
    'share',
    'credit card',
    'rush',
    'south'
]
word = list(choice(words_list).upper())

letters_guessed = []
asterisked = list("*" * len(word))

counter = 0
print(pics(0))

while "*" in asterisked and counter < 6:
    user_letter = input("Enter a letter: ").upper()

    if user_letter in word and user_letter not in letters_guessed:
        print("Good guess!")

        while user_letter in word:
            letter_index = word.index(user_letter)
            asterisked[letter_index] = user_letter
            word[letter_index] = "*"

        letters_guessed.append(user_letter)

    elif user_letter in letters_guessed:
        print("You've already tried this letter, try another one")

    else:
        print("Wrong")
        letters_guessed.append(user_letter)
        counter += 1
        print(pics(counter))

    print("".join(asterisked))
    print("Already guessed:", letters_guessed)

if counter >= 6:
    print("YOU LOSE!")
else:
    print("CONGRATS YOU WIN!")
