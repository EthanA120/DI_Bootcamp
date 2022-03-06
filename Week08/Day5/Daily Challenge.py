# TASK: OOP Quizz
"""
    Part 1: Quizz
    Answer the following questions

        What is a class?
        What is an instance?
        What is encapsulation?
        What is abstraction?
        What is inheritance?
        What is multiple inheritance?
        What is polymorphism?
        What is method resolution order or MRO?


    Part 2: Create a deck of cards class.

    The Deck of cards class should NOT inherit from a Card class.

    The requirements are as follows:

        The Card class should have a suit (Hearts, Diamonds, Clubs, Spades) and a value (A,2,3,4,5,6,7,8,9,10,J,Q,K)
        The Deck class :
            should have a shuffle method which makes sure the deck of cards has all 52 cards and then rearranges them randomly.
            should have a method called deal which deals a single card from the deck. After a card is dealt, it should be removed from the deck.
"""
# class is a "blueprint" for an object, it gives the object it's unique attributes and methods.
# instance is an object that inherit its characteristics from its class.
# encapsulation is a method in witch we store in a "block" of code all the data and functions (like in class).
# abstraction is a process in witch we hide the irrelevant or the sensitive data and make it private.
# inheritance is the ability to use all the information from one class for example to another class.
# we can inherit more than one time to a several classes and repeat the action with the inheriting classes.
# polymorphism is the ability to use a function for example in different shapes of data.
# method resolution order is the way that the program decides what will be the order of inheritance.
from random import shuffle as mix


class Deck:
    def __init__(self):
        self.suit = ["Hearts", "Diamonds", "Clubs", "Spades"]
        self.value = list(range(1, 14))
        self.deck = [(suit, value) for suit in self.suit for value in self.value]
        self.mixed_deck = None
        # print(len(self.deck), self.deck)

    def shuffle(self):
        self.mixed_deck = self.deck.copy()
        mix(self.mixed_deck)
        # print(self.mixed_deck)
        return self.mixed_deck

    def deal(self):
        suit, value = self.mixed_deck.pop(0)
        # print(suit, value)
        return suit, value


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
        print(f"{self.value} of {self.suit}")


deck = Deck()
deck.shuffle()
suit, value = deck.deal()

card = Card(suit, value)

