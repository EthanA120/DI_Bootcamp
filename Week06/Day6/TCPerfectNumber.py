# TASK: Perfect number
"""
    Timed Challenge (30 minutes):

    A perfect number is a positive integer that is equal to the sum of its divisors.
    However, the number itself is not included in the sum.

    Ask the user for a number and print whether or not it is a perfect number. If yes, print True else False.
    Hint: Google perfect numbers

    Example:
    Input -- Enter the number:6
    Output -- True

    Input -- Enter the number:10
    Output --  False
"""
from datetime import datetime

n = int(input("Enter some number: "))  # let user choose a number
sum_of_n = 0

for d in range(1, n):  # we will go from 1 to n
    if n % d == 0:  # if n dividing in d without remainder then d is a divisor of n
        sum_of_n = sum_of_n + d  # and we adding it to the sum

if sum_of_n == n:  # if the sum is equal to n it's a perfect number
    print(True)
else:  # else it's not
    print(False)

task_completion_time = datetime.strptime('30:00', '%M:%S') - datetime.strptime('17:40', '%M:%S')
print(f"\nThis task has been completed within {task_completion_time} minutes")
