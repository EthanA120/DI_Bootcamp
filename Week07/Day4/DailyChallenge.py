# TASK: Exceptions
"""
    Write a function to compute 5/0 and use try/except to catch the exceptions.
    Bonus: use some "Built-in exceptions" of Python, Look here: https://www.programiz.com/python-programming/exceptions
"""
def zero_division():
    return 5 / 0


try:
    zero_division()
except ZeroDivisionError:
    print("Error!")
