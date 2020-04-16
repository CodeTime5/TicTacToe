from abc import ABC, abstractmethod
from Game import Game

class Ui(ABC):
    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        pass

    def run(self):
        pass

class Terminal(Ui):
    def __init__(self):
        self._game = Game()

    def run(self):
        while not self._game.winner:
            print(self._game)
            row = int(input("Enter the row: "))
            col = int(input("Enter the col: "))
            self._game.play(row, col)
        
        print(self._game)
        print(f"The winner was {self._game.winner}. ")

if __name__ == "__main__":
    pass
