# TASK: Exercise 1
"""
    Draw the following pattern using for loops:

      *
     ***
    *****


    Draw the following pattern using for loops:

        *
       **
      ***
     ****
    *****


    Draw the following pattern using for loops:

    *
    **
    ***
    ****
    *****
    *****
     ****
      ***
       **
        *

"""
pic = ""
for x in range(1, 6, 2):
    pic += int((5-x)/2) * " " + x * "*" + "\n"
print(pic)


pic2 = ""
for x in range(1, 6):
    pic2 += (5-x) * " " + x * "*" + "\n"
print(pic2)


pic3 = ""
for x in range(0, 6):
    pic3 += x * "*" + (5-x) * " " + "\n"
print(pic3[0:-1] + pic3[::-1])


# TASK: Exercise 2
"""
    Analyse this code before executing it. Write some comments next to each line.
    Write the value of each variable and their changes, and add the final output.
    Try to understand the purpose of this program.
"""
my_list = [2, 24, 12, 354, 233]
for i in range(len(my_list) - 1):  # running through the list indices except for the last index
    minimum = i  # minimum is te current index
    for j in range(i + 1, len(my_list)):  # running from next index to the last index of the list
        if my_list[j] < my_list[minimum]:  # if next item is smaller than the current one
            minimum = j  # minimum is the next index
            if minimum != i:
                my_list[i], my_list[minimum] = my_list[minimum], my_list[i]  # switch between current and the next items
print(my_list)  # print sorted ascending list
