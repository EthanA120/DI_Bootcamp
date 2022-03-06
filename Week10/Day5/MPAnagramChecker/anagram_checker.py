from itertools import permutations


class AnagramChecker:
    def __init__(self, word: str):
        self.word = word.upper()

        with open("word_list.txt", "r") as read_file:
            self.word_list = [line.replace("\n", "") for line in read_file.readlines()]

    def is_valid_word(self):
        return self.word in self.word_list

    def get_anagrams(self):
        perm = permutations(list(self.word))
        return ["".join(string).lower() for string in list(perm)
                if "".join(string) in self.word_list and "".join(string) != self.word]

    @staticmethod
    def is_anagram(word1: str, word2: str):
        perm = ["".join(string) for string in list(permutations(list(word1)))]
        return word2.upper() in perm
