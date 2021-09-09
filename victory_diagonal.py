board = [["*","*","*"],["#","#","#"],["$","$","$"]]

print ("victory_diagonal.py")
game_over=False

def all_same (cells, symbol):
    rval = True
    for i in range (0,3):
        if cells[i] != symbol:
            rval = False
    return rval
