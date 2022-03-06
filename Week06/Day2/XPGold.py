# TASK: Hello World-I love Python
"""
    Print the following output in one line of code:

    >>> "Hello world"
    >>> "Hello world"
    >>> "Hello world"
    >>> "Hello world"
    >>> "I love python"
    >>> "I love python"
    >>> "I love python"
    >>> "I love python"
"""
print(
    "Hello world\nHello world\nHello world\nHello world\nI love python\nI love python\nI love python\nI love python")


# TASK: What is the Season?
"""
    1. Ask the user to input a month (1 to 12).
    2. Display the season of the month received
        - Spring runs from March (3) to May (5)
        - Summer runs from June (6) to August (8)
        - Autumn runs from September (9) to November (11)
        - Winter runs from December (12) to February (2)
"""
month = input("Enter a month: ").title()

if month in ["March", "April", "May"]:
    print("Spring")
elif month in ["June", "July", "August"]:
    print("Summer")
elif month in ["September", "October", "November"]:
    print("Autumn")
elif month in ["December", "January", "February"]:
    print("Winter")
