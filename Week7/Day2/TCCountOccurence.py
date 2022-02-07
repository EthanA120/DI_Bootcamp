# TASK: Count occurence
"""
    Write a program which takes a string and a character as an input,
    and finds out the number of occurrences the character has in the string.

    String: Programming is cool!
    Character: o
    >> 3

    String: This is a great example
    Character: y
    >> 0
"""
from datetime import datetime


def count_char(string, char):
    print(string.count(char))


count_char("Programming is cool!", "o")
count_char("This is a great example", "y")

task_completion_time = datetime.strptime('15:00', '%M:%S') - datetime.strptime('13:11', '%M:%S')
print(f"\nThis task has been completed within {task_completion_time} minutes")
