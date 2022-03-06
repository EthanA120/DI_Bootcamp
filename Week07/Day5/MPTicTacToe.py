# TASK: Tic Tac Toe
"""
    Create a TicTacToe game in python, where two users can play together.

    Instructions:
        1. The game is played on a grid that’s 3 squares by 3 squares.
        2. Players take turns putting their marks (O or X) in empty squares.
        3. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
        4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.


    Hint:
        To do this project, you basically need to create four functions:
            - display_board() – To display the Tic Tac Toe board (GUI).
            - player_input(player) – To get the position from the player.
            - check_win() – To check whether there is a winner or not.
            - play() – The main function, which calls all the functions created above.

        Note: The 4 functions above are just an example.
            You can implement many more helper functions or choose a completely different approach if you want.


    Tips: Consider the following
        - What functionality will need to occur every turn to make this program work?
        - After contemplating the question above, think about splitting your code into smaller pieces (functions).
        - Remember to follow the single responsibility principle! each function should do one thing and do it well!
"""
from re import sub


def display_board(board):
    # drawing the board matrix
    for arr in board:
        for char in arr:
            if char == 0:
                print(" ", end="")
            elif char == 1:
                print("|", end="")
            elif char == 2:
                print("-", end="")
            else:
                print(char, end="")

        print("")
    print("\n")


def player_input(sign, board):
    indices = {
        "1,1": [0, 1], "1,2": [0, 5], "1,3": [0, 9],
        "2,1": [2, 1], "2,2": [2, 5], "2,3": [2, 9],
        "3,1": [4, 1], "3,2": [4, 5], "3,3": [4, 9],
    }

    mark = sub(r"[()\s]", "", input("Enter row and column (r,c): "))  # input the placement by row and column
    # make sure that a place can't be taken twice
    while board[indices[mark][0]][indices[mark][1]] == sign or mark not in indices.keys():
        print("This place is taken!, try another place")
        mark = sub(r"[()\s]", "", input("Enter row and column (r,c): "))

    board[indices[mark][0]][indices[mark][1]] = sign  # assign player's sign

    return board


def check_win(board, sign):
    board_t = list(zip(*board))  # transpose board

    if (
            (board[0][1] == sign and board[0][1] == board[2][5] and board[2][5] == board[4][
                9]) or  # check main diagonal
            (board[0][9] == sign and board[0][9] == board[2][5] and board[2][5] == board[4][
                1]) or  # check anti-diagonal
            (board[0].count(sign) == 3 or board[2].count(sign) == 3 or board[4].count(sign) == 3) or  # check rows
            (board_t[1].count(sign) == 3 or board_t[5].count(sign) == 3 or board_t[9].count(sign) == 3)  # check columns
    ):
        return False

    else:
        return True


def play():
    # board matrix
    board = [
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
        [2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2],
        [0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0],
    ]

    player = [
        [input("Enter first player's name: "), "X"],
        [input("Enter second player's name: "), "O"]
    ]
    turn = 1

    print("Welcome to Tic Tac Toe!")

    while check_win(board, player[turn][1]):
        if turn == 0:  # switch players turn
            turn = 1
        else:
            turn = 0

        print(f"It's {player[0][turn]}'s turn:")
        display_board(board)
        board = player_input(player[turn][1], board)

    print(f"Game Over!\n{player[0][turn]} is the winner!")


play()
