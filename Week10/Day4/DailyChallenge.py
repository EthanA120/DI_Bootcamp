# TASK: Text Analysis
from collections import Counter
import string
import nltk
from nltk.corpus import stopwords


class Text:
    """
        Download the_stranger.txt

        1. Create a class called Text that takes a string as an argument and store the text in an attribute.
            Implement the following methods:
                - a method to return the frequency of a word in the text
                    (assume words are separated by whitespace) return None or a meaningful message.
                - a method that returns the most common word in the text.
                - a method that returns a list of all the unique words in the text.
                - a class method that returns a Text instance but with a text file:
                    >> Text.from_file('the_stranger.txt')

        2. Create a class called TextModification that inherits from Text.
            Implement the following methods:
                - a method that returns the text without any punctuation.
                - a method that returns the text without any english stop-words (check out what this is !!).
                - a method that returns the text without any special characters.

        Now, use the provided txt file and try using the class you created above.
        Note: Feel free to implement/create any attribute,method or function needed to make this work, be creative :)
    """

    def __init__(self, text: str):
        self.text = text
        self.appearances = Counter(self.text.lower().split(" "))

    def frequency(self, word, display=True):
        """
            a method to return the frequency of a word in the text
            (assume words are separated by whitespace) return None or a meaningful message
        """
        num_of_appearances = self.appearances[word.lower()]
        if display:
            print(f'This word "{word}" appears {num_of_appearances} tims in the text\n')
        return num_of_appearances

    def most_repeated(self, display=True):
        """
            a method that returns the most common word in the text
        """
        word = max(self.appearances, key=self.appearances.get)
        if display:
            print(f'The most repeated word is "{word}" and it appears {self.appearances[word]} times in the text\n')
        return word

    def unique_words(self, display=True):
        """
            a method that returns a list of all the unique words in the text.
        """
        uniques = [word for word in self.appearances if self.appearances[word] == 1]
        if display:
            print(uniques, "\n")
        return uniques

    @classmethod
    def from_file(cls, file_name):
        """
            a classmethod that returns a Text instance but with a text file
        """
        with open(file_name, "r") as read_file:
            return Text(read_file.read())


class TextModification(Text):
    def __init__(self, text: str):
        super().__init__(text)

    def remove_punc(self, display=True):
        """
            a method that returns the text without any punctuation.
        """
        removed_punc = self.text.translate(str.maketrans('', '', string.punctuation))
        if display:
            print(removed_punc, "\n")
        return removed_punc
    
    def non_stop(self, display=True):
        """
            a method that returns the text without any english stop-words
        """
        splinted_text = self.text.split(" ")
        filtered_words = [word for word in splinted_text if word not in stopwords.words('english')]

        if display:
            print(" ".join(filtered_words), "\n")
        return " ".join(filtered_words)

    def not_special(self, display=True):
        """
            a method that returns the text without any special characters
        """
        removed_special = self.text.translate(str.maketrans('', '', r"#$%&*+/<=>@\^_`|~"))
        if display:
            print(removed_special, "\n")
        return removed_special


if __name__ == '__main__':
    some_text = "My string is the best string, and I'll keep this string here! (where I can put it into use)"
    my_string = Text(some_text)

    my_string.frequency("string", )
    my_string.most_repeated()
    my_string.unique_words()
    text_from_file = Text.from_file('the_stranger.txt')

    modified = TextModification(some_text)
    modified.remove_punc()
    modified.non_stop()
    modified_text = "My $+r|ng |s +he be$t $+r|ng, @nd |'ll %eep +h|s $+r|ng here!"
    modified.text = modified_text
    modified.not_special()

    
