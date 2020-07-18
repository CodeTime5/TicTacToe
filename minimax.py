# get any three in a row to win on a 3x3 grid.
from itertools import product
BOARDSIZE = 3
SYMBOLS = ["X", "O"]
EMPTY = "-"
MAXGOAL, MINGOAL = (float("-inf"), max), (float("inf"), min)

# Returns optimal value for current player
def minimax(brd, isMaximizingPlayer):

    boardScore, finished = gameScore(brd)
    if finished:
        return boardScore, None

    bestScore, agg = MAXGOAL if isMaximizingPlayer else MINGOAL
    move = None

    for r,c in product(range(BOARDSIZE), range(BOARDSIZE)):
        if brd[r][c] == EMPTY:
            brd[r][c] = SYMBOLS[isMaximizingPlayer]
            check = agg(bestScore, minimax(brd, not isMaximizingPlayer)[0])
            if check != bestScore:
                bestScore = check
                move = (r, c)
            brd[r][c] = EMPTY

    return bestScore, move


def getMoveChoice():
    while True:
        try:
            c = int(input(f"enter col 1-{BOARDSIZE}:")) - 1
            r = int(input(f"enter row 1-{BOARDSIZE}:")) - 1
            if board[r][c] == EMPTY:
                return r, c
        except:
            pass
        print("invalid choice, please try again...")


def getBoard(brd, rotate):
    brdTemp = zip(*brd) if rotate else brd
    return "\n".join(["".join(line) for line in brdTemp]) + "\n"


def gameScore(brd):
    # return current score (0 for p0 win, 1 for p1 win or 0.5 ongoing or draw)
    # return also True if game over or False if game ongoing
    boardText = getBoard(brd, False) + getBoard(brd, True)
    boardText += "".join([str(brd[x][x]) for x in range(BOARDSIZE)]) + "\n"
    boardText += "".join([str(brd[x][BOARDSIZE - x - 1]) for x in range(BOARDSIZE)])
    checkEnd = [s*BOARDSIZE in boardText for s in SYMBOLS]
    return (0.5, EMPTY not in boardText) if True not in checkEnd else (checkEnd.index(True), True)


def doMove(player):
    row, col = getMoveChoice() if not player else minimax(board, True)[1]
    board[row][col] = SYMBOLS[player]


# MAIN GAME ROUTINE
board = [[EMPTY] * BOARDSIZE for _ in range(BOARDSIZE)]
player = False

while not gameScore(board)[1]:
    print(getBoard(board, False))
    doMove(player)
    player = not player

print(getBoard(board, False))
print("***GAME OVER***")
