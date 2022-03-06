# TASK: Double Dice
"""
    1. Create a function that will simulate the rolling of a dice.
        Call it throw_dice. It should return an integer between 1 and 6.

    2. Create a function called throw_until_doubles.
        1. It should keep throwing 2 dice (using your throw_dice function) until they both land on the same number,
            i.e. until we reach doubles.
            For example: (1, 2), (3, 1), (5,5) then stop throwing, because doubles were reached.
        2. This function should return the number of times it threw the dice in total.
            In the example above, it should return 3.

    3. Create a main function. It should throw doubles 100 times
        (i.e. call your throw_until_doubles function 100 times), and store the results of those function calls
        (in other words, how many throws it took until doubles were thrown, each time) in a collection.
        (What kind of collection? Read below to understand what we will need the data for,
        and this should help you decide which data structure to use).

    4. After the 100 doubles are thrown,
        print out a message telling the user how many throws it took in total to reach 100 doubles.

    5. Also print out a message telling the user the average amount of throws it took to reach doubles.
        Round this off to 2 decimal places.

    6. For example:
        1. If the results of the throws were as follows (your code would do 100 doubles, not just 3):
            1. (1, 2), (3, 1). (5, 5)
            2. (3, 3)
            3. (2, 4). (1, 2), (3, 4), (2, 2)
        2. Then my output would show something like this:
            1. Total throws: 8
            2. Average throws to reach doubles: 2.67.
"""
from random import randint
from statistics import mean


def throw_dice():
    return randint(1, 6)


def throw_until_doubles():
    a = throw_dice()
    b = throw_dice()
    amount_of_throws = 1

    while a != b:
        a = throw_dice()
        b = throw_dice()
        amount_of_throws += 1

    return amount_of_throws


def main():
    list_of_double = []
    for i in range(0, 100):
        list_of_double.append(throw_until_doubles())

    print("Total throws:", sum(list_of_double))
    print("Average throws to reach doubles:", round(mean(list_of_double), 2))


main()
