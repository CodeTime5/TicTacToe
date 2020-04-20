from abc import ABC, abstractmethod
from Game import Game, GameError

class Ui(ABC):
    def __init__(self):
        self._game = Game()
    
    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    pass

class Terminal(Ui):
    def run(self):
        while not self._game.winner:
            print(self._game)
            try:
                row = int(input("Enter the row: "))
                col = int(input("Enter the col: "))
            except ValueError:
                print("Row and Column need to be numbers!")
                continue

            try:
                self._game.play(row, col)
            except GameError as e:
                print(f"Game Error: {e}")
        
        print(self._game)
        if self._game.winner == "DRAW":
            print("Looks like the game was a draw.")
        else:
            print(f"The winner was {self._game.winner}.")

if __name__ == "__main__":
    pass
