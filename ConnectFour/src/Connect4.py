def display(board):
    """Displaying The Board in a systematic pattern
    board -> the main board of the game
    """
    for row in board:
        for element in row:
            print("|", element, end=" ")
        print("|")
        print()


def rows_cols_validation(rows, columns):
    """Checking for a valid input of rows and columns
    rows -> No.of rows in the board
    columns -> No.of columns in the board
    """
    if 4 > rows > 10 and 4 > columns > 10:
        print("You can't play connectFour using mentioned rows/columns")
        exit()


def input_player_decision():
    """Assigning the symbols for the players"""
    player = int(input("You are the player 1 : chose your symbol :\n 1 -> ['O'] \n 2 ->  ['X']\n Enter 1 (or) 2 : "))
    if player == 1:
        return "O"
    elif player == 2:
        return "X"
    else:
        print("You Entered Invalid Choice")
        exit()


def check_rows(board):
    valid1 = "  O    O    O    O  "
    valid2 = "  X    X    X    X  "
    for row in board:
        list_row = ""
        for element in row:
            list_row += str(element) + ""
        print(list_row)
        if list_row.find(valid1) != -1 or list_row.find(valid2) != -1:
            print("YOU WON")
            exit()
        else:
            continue


# def check_game_status(board):

def place_in_order(choice, coin_place, cols, board):
    """To place the coin(Choice) in the proper slot according to the rules
    choice -> O/X placing that coin int the board
    coin_place -> place of the coin that is chosen by the user (player1/player2)
    columns -> reference for the no.of columns in the board
    board -> board of the game
    """
    ind = coin_place - 1
    for i in range(cols):
        if board[(cols - 1) - i][ind] == "  -  ":
            board[(cols - 1) - i][ind] = "  " + choice + "  "
            return
        else:
            continue


if __name__ == "__main__":
    board_rows = int(input("Enter no.of rows of board : "))
    board_columns = int(input("Enter no.of columns of the board : "))
    rows_cols_validation(board_rows, board_columns)  # Checking for Rows and Columns Validation
    game_board = [["  -  " for i in range(board_columns)] for j in range(board_rows)]


    place_in_order("X", 1, board_columns, game_board)
    place_in_order("X", 5, board_columns, game_board)
    place_in_order("X", 3, board_columns, game_board)
    place_in_order("X", 4, board_columns, game_board)
    print(game_board)
    display(game_board)
    check_rows(game_board)


    # player1 = input_player_decision()
    # player2 = None
    #
    # if player1 == "O":
    #     player2 = "X"
    # else:
    #     player2 = "O"
    #
    #
    # c_num = int(input("Enter the column number to drop your choice : "))
