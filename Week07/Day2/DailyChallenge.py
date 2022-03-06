# TASK: Solve the Matrix
"""
    Hint: Look at the remote learning “Matrix” videos

    The matrix is a grid of strings (alphanumeric characters and spaces) with a hidden message in it.
    To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column,
    select only the alpha characters and connect them,
    then he replaces every group of symbols between two alpha characters by a space.

    Using his technique, try to decode this matrix:

        7i3
        Tsi
        h%x
        i #
        sM
        $a
        #t%
        ^r!
"""
message = [
    "7i3",
    "Tsi",
    "h%x",
    "i #",
    "sM ",
    "$a ",
    "#t%",
    "^r!"
]

transpose = list(zip(*message))  # replace between i and j using tuples
trans_string = "".join("".join(li) for li in transpose)  # convert the tuples to string

message_arranged = ""
not_alpha = ""
i = 0
while i < len(trans_string):  # running across the list
    if trans_string[i].isalpha():  # if the char is an alphabet we will add it to the final string
        message_arranged += trans_string[i]
        i += 1

    else:
        j = i  # starting from i's location
        while j < len(trans_string):
            if not trans_string[j].isalpha():  # as long as the chars is not alphabet
                not_alpha += trans_string[i]  # add all the following non-alphabet chars
            else:
                break  # when we encounter an alphabet char
            j += 1

        if len(not_alpha) > 1:  # if there is a sequence of non-alphabet chars they will be replaced with whitespace
            message_arranged += " "

        i = j  # continue from where we stopped
        not_alpha = ""  # reset the non-alpha counter for the next time

print(message_arranged)
