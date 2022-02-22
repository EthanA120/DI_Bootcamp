# TASK: Built-in functions
class BuiltIns:
    """
        Python has many built-in functions.
        If you feel that you don’t know how to properly implement them take a look at the python documentation online.

            1. Write a program which prints the results of the following python built-in functions:
                abs(), int(), input().

            2. Using the __doc__ dunder method create your own documentation which explains the execution of your code.
                Take a look at the doc method on google for help.
    """

    @staticmethod
    def built_ins():
        print(abs(-1))
        print(int("1"))
        print(input("Enter something to print: "))


print(BuiltIns.__doc__)


# TASK: Currencies
class Currency:
    """
        Create the code which will output the results below.
        Hint : When adding 2 currencies which don’t share the same label you should raise an error.

        >> c1 = Currency('dollar', 5)
        >> c2 = Currency('dollar', 10)
        >> c3 = Currency('shekel', 1)
        >> c4 = Currency('shekel', 10)

        >> str(c1)
        '5 dollars'

        >> int(c1)
        5

        >> repr(c1)
        '5 dollars'

        >> c1 + 5
        10

        >> c1 + c2
        15

        >> c1
        5 dollars

        >> c1 += 5
        >> c1
        10 dollars

        >> c1 += c2
        >> c1
        20 dollars

        >> c1 + c3
        TypeError: Cannot add between Currency type <dollar> and <shekel>
    """

    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

        if self.amount != 1:
            self.currency += "s"

    def __str__(self):
        return f"{self.amount} {self.currency}"

    def __int__(self):
        return self.amount

    def __repr__(self):
        return repr(f"{self.amount} {self.currency}")

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            return self.amount + other
        else:
            if self.currency == other.currency:
                return self.amount + other.amount
            else:
                raise TypeError

    def __iadd__(self, other):
        if type(other) == int or type(other) == float:
            self.amount = self.amount + other
            return self

        else:
            if self.currency == other.currency:
                self.amount = self.amount + other.amount
                return self
            else:
                raise TypeError


c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(str(c1))
print(int(c1))
print(repr(c1))
print()

print(c1 + 5)
print(c1 + c2)
print(c1)
print()

c1 += 5
print(c1)

c1 += c2
print(c1)
print()

try:
    c1 + c3
except TypeError:
    print("TypeError")
