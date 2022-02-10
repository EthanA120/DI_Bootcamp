# TASK: Sorting
"""
    1. Write a program that accepts a comma separated sequence of words as input,
        the program prints the words in a comma-separated sequence after sorting them alphabetically.
    2. Use List Comprehension

    Suppose the following input is supplied to the program:
        without,hello,bag,world

    Then, the output should be:
        bag,hello,without,world
"""
words = "without,hello,bag,world"
sorted_words = sorted(words.split(","))
[print(word, end=",") if word != sorted_words[-1] else print(word) for word in sorted_words]
