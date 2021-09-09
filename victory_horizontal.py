board = [["*","*","*"],["#","#","#"],["$","$","$"]]

print ("victory_horizontal.py")
game_over=False

def all_same (cells, symbol):
    rval = True
    for i in range (0,3):
        if cells[i] != symbol:
            rval = False
    return rval

#check lines
for i in range(0,3):
    print (board [i])
    print (all_same (board[i], board[i][0]))

