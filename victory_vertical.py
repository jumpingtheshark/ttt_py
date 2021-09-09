board = [["1","#","13"],["21","#","23"],["*","#","$"]]


game_over=False

def all_same (cells, symbol):
    rval = True
    for i in range (0,3):
        if cells[i] != symbol:
            rval = False
    return rval

#check columns
l=[]
for i in range (0,3):
    l=[]
    for j in range(0,3):
        l.append(board[i][j])
    print (l)
    print(all_same(l, board[i][0]))
