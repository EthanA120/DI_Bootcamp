# TASK: Box of stars
"""
    Write a function named box_printer that takes any amount of strings (not in a list) and prints them,
    one per line, in a rectangular frame.

    For example calling box_printer("Hello", "World", "in", "reallylongword", "a", "frame") will result as:

        >> ******************
        >> * Hello          *
        >> * World          *
        >> * in             *
        >> * reallylongword *
        >> * a              *
        >> * frame          *
        >> ******************
"""
def box_printer(*user_words):
    max_length = 0
    for word in user_words:
        if len(word) > max_length:
            max_length = len(word)

    framed_words = ["*" * (max_length + 4)]
    for word in user_words:
        framed_words.append(f"* {word + ' ' * (max_length - len(word))} *")

    framed_words.append(framed_words[0])

    print("\n".join(framed_words))


box_printer("Hello", "World", "in", "reallylongword", "a", "frame")


# TASK: Exercise 2
""" 
    Analyse the code before executing it.
    What is the purpose of this code?
"""
def insertion_sort(alist):
    for index in range(1, len(alist)):  # from the second to the last indices in the list

        current_value = alist[index]  # take element and index
        position = index

        while position > 0 and alist[position - 1] > current_value:
            # as long as index bigger than 0 and previous element bigger than current element
            alist[position] = alist[position - 1]  # current is now previous
            position = position - 1

        alist[position] = current_value  # previous is now current


# The smaller value goes to the head of the list and the bigger goes to the end of it.
# the program sorts the values in the list from the smaller value to the bigger value

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertion_sort(alist)
print(alist)
