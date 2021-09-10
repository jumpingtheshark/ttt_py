#print("victory.py")
game_over = False


def all_same(cells, symbol):
    rval = True
    for i in range(0, 3):
        if cells[i] != symbol:
            rval = False
    return rval


def test_win_right(board, symbol):
    # right
    l = []
    for i in range(0, 3):
        l.append(board[i][i])
    rval=all_same(l, symbol)
    return rval

#left

def test_win_left(board, symbol):
    l = []
    j=2
    for i in range(0,3):
        l.append(board[i][j])
        j=j-1
    #print (l)
    rval=all_same(l, symbol)
    return rval

def test_win_horizontal(board, symbol):
    for i in range(0,3):

        l=board[i]
        rval= (all_same ( l, symbol))
        if rval:
            return True

    return  False


def test_win_vertical (board, symbol):
    # check columns
    l = []
    for i in range(0, 3):
        l = []
        for j in range(0, 3):
            l.append(board[j][i])
        rval=all_same(l, symbol)
        if rval:
            return True

    return  False

#board = [["1", "*", "1"], ["#", "2", "#"], ["3", "$", "X"]]
#test_win_left(board)


