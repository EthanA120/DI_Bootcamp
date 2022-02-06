# TASK: Caesar Cypher
"""
    In cryptography, a Caesar cipher is one of the simplest and most widely known encryption techniques.
    It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter,
    some fixed number of positions down the alphabet.

    For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.
    The method is named after Julius Caesar, who used it in his private correspondence.

    Create a python program that encrypts and decrypts messages with ceasar cypher,
    the user entries the program, and then the program asks him if he wants to encrypt or decrypt,
    and then execute encryption/decryption on a given message and a given shift.

    Check out this tutorial: https://cryptii.com/pipes/caesar-cipher

    Hint: for letter in text:
        cypher_text += chr(ord(letter) + 3)
"""
import string

message = input("Enter the message: ")
program_type = input("To encrypt enter 'E', to decrypt enter 'D': ").upper()
shift = int(input("Enter shift (numeric value): "))

if shift > 26:
    shift = shift - (shift // 26) * 26  # Never exceed 26 (after 26 comes 1)
if shift < 0:
    shift = (-shift // 26) * 26 + shift  # Never exceed -26 (after -26 comes -1)

cypher_text = ""
shift_border = []
sign = 0
encrypt = -1

if program_type == "E":  # if we want to encrypt
    sign = 1  # to be used later as the sign of operator (+ or -)
    encrypt = 1  # an indicator to know what border we should be careful not to cross (upper or lower)

elif program_type == "D":  # if we want to decrypt
    sign = -1
    encrypt = 0

for letter in message:
    if letter.isupper():
        shift_border = [65, 90]  # ascii for letters between A to Z
    elif letter.islower():
        shift_border = [97, 122]  # ascii for letters between a to z

    shifted_letter = ord(letter) + sign * shift  # ascii number for letter +- shift (can exceed shift_border values)

    if letter not in string.punctuation + " ":  # special letters and whitespace
        if encrypt and shifted_letter > shift_border[encrypt] or not encrypt and shifted_letter < shift_border[encrypt]:
            # need to be careful not to cross upper and lower borders when encrypt or decrypt respectively
            cypher_text += chr(shifted_letter - 26 * sign)

        else:
            cypher_text += chr(shifted_letter)  # simply shift the letter if we don't exceed any border

    else:
        cypher_text += letter  # if it's a special letter or whitespace add it as it is

print(cypher_text)
