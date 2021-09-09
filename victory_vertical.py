board = [["*","*","*"],["#","#","#"],["$","$","$"]]


game_over=False

def all_same (cells, symbol):
    rval = True
    for i in range (0,3):
        if cells[i] != symbol:
            rval = False
    return rval

#check columns
l=[]
for i in range(0,3):
    l.append(board[i][0])

print (l)
print(all_same(l, board[i][0]))
