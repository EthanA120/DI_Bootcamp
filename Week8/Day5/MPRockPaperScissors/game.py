# TASK: Rock, Paper, Scissors
"""
    Rock-paper-scissors is an old game that can be played between two people. You can read about it in wikipedia:
    https://en.wikipedia.org/wiki/Rock_paper_scissors

    We will create a game for the user to play Rock-paper-scissors against the computer.

        -The user will input his/her move (rock/paper/scissors),
        -and the computer will select either rock, paper or scissors at random.
        -We will then compare the user’s move with the computer’s move, and determine the results of the game:
            -The user won
            -The computer won (the user lost)
            -A draw (tie)

    We will print the outcome of each game: the user’s choice, the computer’s choice, and the result.

    The user will be able to play again and again.
    Once the user decides to exit the program, we will print a summary of the outcomes of all the games:
        how many times they won, lost or and tied the computer.

    An example for output can be found in the Example.bmp file


    Instructions:
    1. Create a new directory for the game. Inside it, create 2 files:
        1. rock-paper-scissors.py – this will contain functions to show the main menu,
            handle user’s input, and show the game summary before exiting.
        2. game.py – this will contain a Game class which will have functions to play a single game of
            rock-paper-scissors against the computer, determine the game’s result, and return the result.


    Steps:
    Part I - game.py

    1. game.py – this file/module should contain a class called Game. It should have 4 methods:
        1. get_user_item(self) – Ask the user to select an item (rock/paper/scissors).
            Keep asking until the user has selected one of the items – use data validation and looping.
            Return the item at the end of the function.

        2. get_computer_item(self) – Select rock/paper/scissors at random for the computer.
            Return the item at the end of the function. Use python’s random.choice() function (read about it online).

        3. get_game_result(self, user_item, computer_item) – Determine the result of the game.
            Parameters:
                - user_item – the user’s chosen item (rock/paper/scissors)
                - computer_item – the computer’s chosen (random) item (rock/paper/scissors)
                - Return either win, draw, or loss. Where win means that the user has won,
                    draw means the user and the computer got the same item, and loss means that the user has lost.

        4. play(self) – the function that will be called from outside the class (ie. from rock-paper-scissors.py).
            It will do 3 things:
            1. Get the user’s item (rock/paper/scissors) and remember it

            2. Get a random item for the computer (rock/paper/scissors) and remember it

            3. Determine the results of the game by comparing the user’s item and the computer’s item
                1. Print the output of the game; something like this: “You selected rock. The computer selected paper.
                You lose”, “You selected scissors. The computer selected scissors. You drew!”

                1. Return the results of the game as a string: win;draw;loss;, where win means that the user has won,
                draw means the user and the computer got the same item, and loss means that the user has lost.


    Part II - rock-paper-scissors.py

    1. rock-paper-scissors.py: create 3 functions
        1. get_user_menu_choice() - this should display a simple menu, get the user’s choice (with data validation),
            and return the choice. No looping should occur here.
        The possibles choices are : Play a new game or Show scores or Quit

        2. print_results(results) – this should print the results of the games played.
            It should have a single parameter named results;
            which will be a dictionary of the results of the games played.
            It should display these results in a user-friendly way, and thank the user for playing.


        Note: results should be in this form: {win: 2,loss: 4,draw: 3}.
            Bear in mind that this dictionary will need to be created and populated in some other part of our code,
            and passed in to the print_results function at the right time.

        3. main() - the main function. It should take care of 3 things:
            1. Displaying the menu repeatedly, until the user types in the value to exit the program: ‘x’ or ‘q’,
                whatever you decide. (Make use of the get_user_menu_choice function)

            2. When the user chooses to play a game:
                - Create a new Game object (see below), and call its play() function,
                    receiving the result of the game that is returned.
                - Remember the results of every game that is played.

            3. When the user chooses to exit the program,
                call the print_results function in order to display a summary of all the games played.
"""
from random import choice


class Game:
    def __init__(self):
        self.options = ["R", "P", "S"]
        self.options_dict = {"R": "Rock", "P": "Paper", "S": "Scissors"}

    def get_user_item(self):
        player_input = ""
        while player_input not in self.options:
            player_input = input("choose (R)ock, (P)aper or (S)cissors: ").upper()
            return player_input

    def get_computer_item(self):
        computer_choice = choice(self.options)
        return computer_choice

    def get_game_result(self, user_item, computer_item):
        user_index = self.options.index(user_item)
        computer_index = self.options.index(computer_item)
        abs_distance = abs(self.options.index(user_item) - self.options.index(computer_item))

        if user_item == computer_item:
            return "Draw"
        elif abs_distance == 1 and user_index > computer_index or abs_distance == 2 and user_index < computer_index:
            return "Win"
        else:
            return "Lose"

    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(user_item, computer_item)
        print(
            f"You selected {self.options_dict[user_item]}.\n"
            f"The computer selected {self.options_dict[computer_item]}.\n"
            f"It's a {result}\n"
        )
        if result == "Win":
            num_result = 1
        elif result == "Lose":
            num_result = -1
        else:
            num_result = 0

        return result, num_result


if __name__ == '__main__':
    rps = Game().play()
