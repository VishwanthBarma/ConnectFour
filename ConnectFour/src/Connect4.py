def display(board, columns):
    """Displaying The Board in a systematic pattern
    board -> the main board of the game
    """
    for i in range(columns):
        print("     ", (i + 1), end=" ")
    print()

    num = 1
    for row in board:
        print(str(num), end=" ")
        for element in row:
            print("|", element, end=" ")
        print("|")
        print()
        num += 1


def rows_cols_validation(rows, columns):
    """Checking for a valid input of rows and columns
    rows -> No.of rows in the board
    columns -> No.of columns in the board
    """
    if 4 >= rows >= 10 and 4 >= columns >= 10:
        print("You can't play connectFour using mentioned rows/columns")
        exit()


def input_player_decision():
    """Assigning the symbols for the players"""
    option = int(input("You are the player-1 \nchoose your symbol :\n1 -> ['O'] \n2 ->  ['X']\nEnter 1 (or) 2 : "))
    if option == 1:
        return "O"
    elif option == 2:
        return "X"
    else:
        print("You Entered Invalid Choice")
        exit()


def check_left_diagonal(slot, board, rows, columns):
    """Checking the left diagonal in the board (\\)
    slot -> Return list from the place_in_order function
    board -> Main Board from the game
    rows -> Rows in the game board
    columns -> Columns in the game board
    """
    r1, r2 = slot[0], slot[0] - 1
    c1, c2 = slot[1], slot[1] - 1
    lower_string = ""
    upper_string = ""
    while r1 < columns and c1 < rows:
        element = board[r1][c1]
        lower_string += str(element) + ""
        r1 += 1
        c1 += 1
    while r2 >= 0 and c2 >= 0:
        element = board[r2][c2]
        upper_string += str(element) + ""
        r2 -= 1
        c2 -= 1
    upper_string = upper_string[::-1]
    final_string = upper_string + lower_string
    valid1 = "  O    O    O    O  "
    valid2 = "  X    X    X    X  "
    if final_string.find(valid1) != -1 or final_string.find(valid2) != -1:
        return 1
    else:
        return 0
        # print("YOU WON")
        # exit()


def check_right_diagonal(slot, board, rows, columns):
    """Checking the right diagonal in the board (//)
    slot -> Return list from the place_in_order function
    board -> Main Board from the game
    rows -> Rows in the game board
    columns -> Columns in the game board
    """
    r1, r2 = slot[0], slot[0] - 1
    c1, c2 = slot[1], slot[1] + 1
    lower_string = ""
    upper_string = ""
    while r1 < rows and c1 >= 0:
        element = board[r1][c1]
        lower_string += str(element) + ""
        r1 += 1
        c1 -= 1
    while r2 >= 0 and c2 < columns:
        element = board[r2][c2]
        upper_string += str(element) + ""
        r2 -= 1
        c2 += 1
    lower_string = lower_string[::-1]
    final_string = lower_string + upper_string
    valid1 = "  O    O    O    O  "
    valid2 = "  X    X    X    X  "
    if final_string.find(valid1) != -1 or final_string.find(valid2) != -1:
        return 1
    else:
        return 0
        # print("YOU WON")
        # exit()


def check_rows(slot, board, rows):
    """Checking for win, in case condition satisfies in a row
    slot -> Returned value from function place_in_order [row, column]
    board -> Main Board of the game
    rows -> No of rows in the game board
    """
    valid1 = "  O    O    O    O  "
    valid2 = "  X    X    X    X  "
    string_row = ""
    for i in range(rows):
        element = board[slot[0]][i]   # here slot[0] indicates the row value of the placed slot
        string_row += str(element) + ""
    if string_row.find(valid1) != -1 or string_row.find(valid2) != -1:
        return 1
    else:
        return 0
        # print("YOU WON")
        # exit()


def check_columns(slot, board, columns):
    """Checking for win, in case condition satisfies in a column
    slot -> Returned value from function place_in_order [row, column]
    board -> Main Board of the game
    columns -> No of columns in the game board
    """
    valid1 = "  O    O    O    O  "
    valid2 = "  X    X    X    X  "
    string_column = ""
    for i in range(columns):
        element = board[i][slot[1]]  # here slot[1] indicates the column value of the placed slot
        string_column += str(element) + ""
    if string_column.find(valid1) != -1 or string_column.find(valid2) != -1:
        return 1
    else:
        return 0
        # print("YOU WON")
        # exit()


def check_game_status(slot, board, rows, columns):
    c1 = check_rows(slot, board, rows)  # Checking in rows
    c2 = check_columns(slot, board, columns)  # Checking in columns
    c3 = check_right_diagonal(slot, board, rows, columns)  # Checking in 1st diagonal
    c4 = check_left_diagonal(slot, board, rows, columns)  # Checking in 2nd diagonal
    if c1 == 1 or c2 == 1 or c3 == 1 or c4 == 1:
        return 1
    else:
        return 0


def place_in_order(choice, coin_place, cols, board):
    """To place the coin(Choice) in the proper slot according to the rules
    choice -> O/X placing that coin int the board
    coin_place -> place of the coin that is chosen by the user (player1/player2)
    columns -> reference for the no.of columns in the board
    board -> board of the game
    <--Returns the Slot of Placed Coin [row, column]-->
    """
    ind = coin_place - 1
    for i in range(cols):
        a = (cols - 1) - i
        if board[a][ind] == "  -  ":
            board[a][ind] = "  " + str(choice) + "  "
            return [int(a), int(ind)]  # Returning the row and column number of the slot
        else:
            continue


if __name__ == "__main__":
    board_rows = int(input("Enter no.of rows of board between (4-10) inclusively : "))
    board_columns = int(input("Enter no.of columns of the board between (4-10) inclusively : "))
    rows_cols_validation(board_rows, board_columns)  # Checking for Rows and Columns Validation
    game_board = [["  -  " for i in range(board_columns)] for j in range(board_rows)]
    # player1, player2 = None, None
    player1 = input_player_decision()  # Assigning symbols for players according to the user input
    player2 = ""
    if player1 == "O":
        player2 = "X"
    else:
        player2 = "O"
    display(game_board, board_columns)  # Displaying the board
    play_game = True
    turn = [player1, player2]
    turn1 = turn[0]
    turn1_name = "Player-1"
    while play_game:
        print("Enter 'q' for quit the game")
        choice_of_player = int(input("Enter the column number to drop your choice ({}): ".format(turn1_name)))

        # Quiting the code if the player enters 'q' in selecting the columns
        if choice_of_player == "q" or choice_of_player == "Q":
            exit()

        # Checking for invalid column selection by the user
        if choice_of_player < 1 or choice_of_player > board_columns:
            print("Input is out of range- Invalid Input")
            continue
        #  Placing the coin in the board
        coin_slot = place_in_order(turn1, choice_of_player, board_columns, game_board)

        # Displaying the Game Board
        display(game_board, board_columns)

        # Checking for game status
        result = check_game_status(coin_slot, game_board, board_rows, board_columns)
        if result == 1:
            print(turn1_name, " Won The Game")
            exit()

        # Changing turns of te player in the output screen
        if turn1 == turn[0]:
            turn1 = turn[1]
            turn1_name = "Player-2"
        else:
            turn1 = turn[0]
            turn1_name = "Player-1"
