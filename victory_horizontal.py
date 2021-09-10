#board = [["*","*","*"],["#","#","#"],["$","$","$"]]

print ("victory_horizontal.py")
game_over=False

def all_same (cells, symbol):
    rval = True
    for i in range (0,3):
        if cells[i] != symbol:
            rval = False
    return rval

#check lines
def test_win_horizontal(board, symbol):
    for i in range(0,3):
        print (all_same ("X", board[i][0]))

