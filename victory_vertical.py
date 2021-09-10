board = [["*","#","$"],["*","#","$"],["*","#","$"]]

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
        l.append(board[j][i])
    print (l)
    print(all_same(l, l[i][0]))
