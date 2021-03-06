import random
from victory import test_win_right, test_win_left, test_win_horizontal, test_win_vertical

board = [["*","*","*"],["*","*","*"],["*","*","*"]]

#print (board )

def check_spot(row, column):
    pass

def show_board ():
    print ("============================")
    print("============================")
    for row in board:
        for cell in row:
            print (cell, end="")
            print ("|", end ="")
        print ('\n')
'''
def add_element (row, column, side):
    # check first if it's already is being taken
    if spot_free(row, column):
        board[row][column]="X"

'''

def spot_free(row, column):
    if board[row][column] != "*":
        return False
    else:
        return True

def ask_user():
    row = int(input ("which row?"))
    column = int(input ("which column"))
    if spot_free (row, column) == False:
        print ("sorry, that spot's taken")
        return False
    else:
        board[row][column]= "X"
        return True

def computer_move():
    spot_found=False
    while not spot_found:
        column = random.randint(0,2)
        row =random.randint(0, 2)
        if spot_free(row, column)==True:
            board[row][column]="0"
            spot_found=True

def check_victory(symbol):
    # there are 7 ways to win in tic tac toe
    rval = False
    rval = test_win_left(board, symbol)
    if rval:
        return rval

    rval = test_win_right(board,symbol)
    if rval:
        return rval

    rval = test_win_horizontal(board, symbol)
    if rval:
        return rval

    rval = test_win_vertical(board, symbol)
    return rval


def main():
    show_board()
    while True:
        valid_input= False
        while valid_input == False:
            valid_input = ask_user()
        print ("input accepted")
        show_board()

        if (check_victory("X")==True):
            print ("we have victory, no point in going further!!! ")
            break

        input ("press enter for the computer move please")
        computer_move()
        show_board()

        if (check_victory("0") == True):
            print ("we have victory, no point in going further!!! ")
            break

    #add_element(1,1)
    #show_board()


main()

