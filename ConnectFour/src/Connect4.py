# 1.Display Board Accourding to rows and columns
def display(rows, columns, board):
    board = [["  -  " for i in range(columns)] for j in range(rows)]

    for row in board:
        print(row)

# display(5,5)

# 2.Taking Input From The User : Rows and Columns