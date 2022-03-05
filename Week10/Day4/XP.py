# TASK: Random Sentence Generator
"""
    Description: In this exercise we will create a random sentence generator.
    We will do this by asking the user how long the sentence should be and then printing the generated sentence.

    Hint : The generated sentences do not have to make sense.

        Download this word list

        Save it in your development directory.

        Create a function called get_words_from_file.
        This function should read the file’s content and return the words as a collection.
        What is the correct data type to store the words?

        Create another function called get_random_sentence which takes a single parameter called length.
        The length parameter will be used to determine how many words the sentence should have.
        The function should:
            - use the words list to get your random words.
            - the amount of words should be the value of the length parameter.

        Take the random words and create a sentence (using a python method), the sentence should be lowercase.

        Create a function called main which will:
        Print a message explaining what the program does.

        Ask the user how long they want the sentence to be.
        Acceptable values are: an integer between 2 and 20.
        Validate your data and test your validation!
            If the user inputs incorrect data, print an error message and end the program.
            If the user inputs correct data, run your code.
"""
from random import choice


def get_words_from_file():
    """
        This function should read the file’s content and return the words as a collection.
        What is the correct data type to store the words?
    """
    with open("word_list.txt", "r") as read_file:
        word_list = [line.replace("\n", "") for line in read_file.readlines()]
    return word_list


def get_random_sentence(length):
    """
    Create another function called get_random_sentence which takes a single parameter called length.
    The length parameter will be used to determine how many words the sentence should have.
    The function should:
        - use the words list to get your random words.
        - the amount of words should be the value of the length parameter.
    """
    strings = []
    words_list = get_words_from_file()

    for i in range(length):
        strings.append(choice(words_list))

    return " ".join(strings).lower()


def main():
    print("in this program you can use a random sentence generator."
          "You will do this by asking the user how long the sentence should be,"
          "and then the program will print the generated sentence\n")

    user_input = int(input("Enter the wanted sentence length (2-20 chars): "))
    if 2 <= user_input <= 20:
        rnd_sentence = get_random_sentence(user_input)
        print(rnd_sentence)
    else:
        try:
            raise ValueError
        except ValueError:
            print("The input must be between 2 to 20 characters, Good bye!")


if __name__ == '__main__':
    main()
