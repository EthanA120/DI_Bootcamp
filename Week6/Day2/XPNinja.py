# TASK: Use the terminal
"""
    Windows: Run this command in the terminal to open a python console:
    >>> "python"

    Mac: Run this command in the terminal to open a python console:
    >>> "$ python3"

        Read about the PATH variable. Try to explain why you can call python3 if you aren’t in the executable directory.
        PATH explanation can be found here: https://linuxconfig.org/linux-path-environment-variable
"""
# From the link:
# Adding a directory to the PATH variable will enable you to call on your program or script from anywhere in the system,
# without needing to specify the path to where you’ve stored it.


# TASK: Alias
"""
    Read about alias, and try to open a python console with the command:
    >>> "$ py"
"""
# If you are using the Windows PowerShell and not the command prompt, you can use the following code:
# >>> "Set-Alias -Name python3 -Value python"
#
# or use the following code:
# >>> "Set-Alias -Name python3 -Value "C:\Python39\python.exe""
#
# Note that this is a temporary Alias for the current session, to make it permanent;
# you have to copy the above command into an empty text file,
# then name it Profile.ps1 file and copy it to one of the following folders:
#
#     if you are using PowerShell 7:
#     >>> {My Documents Folder}/PowerShell
#
#     if you are using Windows PowerShell which comes by default in Windows 10:
#     >>> {My Documents Folder}/WindowsPowerShell
#
#     or inside the installation folder of PowerShell, which can be figured out by:
#     >>> cd $PSHOME\


# TASK: Outputs
"""
    Predict the output of the following code snippets:

    >>> 3 <= 3 < 9

    >>> 3 == 3 == 3

    >>> bool(0)

    >>> bool(5 == "5")

    >>> bool(4 == 4) == bool("4" == "4")

    >>> bool(bool(None))

    x = (1 == True)
    y = (1 == False)
    a = True + 4
    b = False + 10

    print("x is", x)
    print("y is", y)
    print("a:", a)
    print("b:", b)
"""
# 3 <= 3 < 9                        :   True
# 3 == 3 == 3                       :   True
# bool(0)                           :   False
# bool(5 == "5")                    :   False
# bool(4 == 4) == bool("4" == "4")  :   True
# bool(bool(None))                  :   False

# x = (1 == True)                   :   x = True
# y = (1 == False)                  :   y = False
# a = True + 4                      :   a = 5
# b = False + 10                    :   b = 10

# print("x is", x)                  :   >>> "x is True"
# print("y is", y)                  :   >>> "y is False"
# print("a:", a)                    :   >>> "a: 5"
# print("b:", b)                    :   >>> "b: 10"


# TASK: How many characters in a sentence?
"""
    Use python to find out how many characters are in the following text, use a single line of code (beyond the 
    establishment of your my_text variable). 

    my_text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
           sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
           Ut enim ad minim veniam, quis nostrud exercitation ullamco 
           laboris nisi ut aliquip ex ea commodo consequat. 
           Duis aute irure dolor in reprehenderit in voluptate velit 
           esse cillum dolore eu fugiat nulla pariatur. 
           Excepteur sint occaecat cupidatat non proident, 
           sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
my_text = """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit,
    sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
    Ut enim ad minim veniam, quis nostrud exercitation ullamco 
    laboris nisi ut aliquip ex ea commodo consequat. 
    Duis aute irure dolor in reprehenderit in voluptate velit 
    esse cillum dolore eu fugiat nulla pariatur. 
    Excepteur sint occaecat cupidatat non proident, 
    sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
print(len(my_text))


# TASK: Longest word without a specific character
"""
    1. Keep asking the user to input the longest sentence they can without the character “A”.
    2. Each time a user successfully sets a new longest sentence, print a congratulations message.
"""
# Loop from here to the end of the code
user_record = 0
user_text = input("Enter the longest sentence you can without the character “A”: ")
a_location = user_text.find("a")

if a_location > user_record:
    print("congratulations! It's a new record")
    user_record = a_location
