# TASK: Reverse the Sentence
"""
    Write a program to reverse the sentence wordwise.

    Input:
    You have entered a wrong domain
    Output:
    domain wrong a entered have You
"""
from datetime import datetime

sentence = "You have entered a wrong domain"  # a sentence for example, can also be an input

sentence_list = sentence.split(" ")[::-1]  # split words by whitespace, turn to list and reverse the words with slicing
reversed_sentence = " ".join(sentence_list)  # join the words into a string, now the sentence is reversed
print(reversed_sentence)

task_completion_time = datetime.strptime('30:00', '%M:%S') - datetime.strptime('17:40', '%M:%S')
print(f"\nThis task has been completed within {task_completion_time} minutes")