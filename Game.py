class Game:
    EMPTY = " "
    DIM = 3
    P1 = "o"
    P2 = "x"

    def __init__(self):
        self._board = [[Game.EMPTY for _ in range(Game.DIM)] for _ in range(Game.DIM)]
        self._player = Game.P1

    def __repr__(self):
        result = "  " + " ".join(str(i+1) for i in range(Game.DIM))
        for row in range(Game.DIM):
            result += f"\n{row + 1} {self._board[row][0]}|{self._board[row][1]}|{self._board[row][2]}"
            if row + 1 != Game.DIM:
                result += "\n  -----"
        result += f"\n\n{self._player} turn to play"
        return result

    def play(self, row, col):
        row += -1
        col += -1
        self._board[row][col] = self._player
        self._player = Game.P2 if self._player is Game.P1 else Game.P1
    
    @property
    def winner(self):
        for p in [Game.P1, Game.P2]:
            for row in range(3):
                if all(self._board[row][col] is p for col in range(3)):
                    return p
            for col in range(3):
                if all(self._board[row][col] is p for row in range(3)):
                    return p
            ## Diagonals
            if all(self._board[i][i] is p for i in range(3)):
                return p
            if all(self._board[i][2 - i] is p for i in range(3)):
                return p
        
        ## No winner
        return None


if __name__ == "__main__":
    pass
