from tkinter import Button, Tk, Toplevel, Frame, N,S,E,W,X,Y, LEFT,RIGHT, END, Scrollbar, Text, Message, Grid, StringVar
from Game import Game, GameError
from sys import stderr
from itertools import product
from abc import ABC, abstractmethod

class Ui(ABC):
    @abstractmethod
    def run(self):
        raise NotImplementedError

class Gui(Ui):
    def __init__(self):
        root = Tk()
        root.title("Tic Tac Toe - Menu")
        frame = Frame(root)
        frame.pack(fill=X)

        Button(
            frame,
            text = "Play Game",
            command = self.play_callback
        ).pack(fill=X)

        Button(
            frame,
            text = "Show Help",
            command = self.help_callback
        ).pack(fill=X)

        Button(
            frame,
            text = "Quit",
            command = root.quit
        ).pack(fill=X)

        self._root = root
    
    def play_callback(self):
        self._game = Game()
        game_window = Toplevel(self._root)
        game_window.title("Tic Tac Toe - Game")
        frame = Frame(game_window)
        frame.grid(row=0, column=0)

        dim = Game.DIM
        self._buttons = [[None for _ in range(dim)] for _ in range(dim)]
        for row, col in product(range(dim), range(dim)):
            b = StringVar()
            b.set(self._game.at(row+1, col+1))

            cmd = lambda r=row,c=col : self.play_and_refresh(r, c)

            Button(
                frame,
                textvariable = b,
                command = cmd
            ).grid(row=row, column=col)

            self._buttons[row][col] = b
        
        Button(game_window, text="Dismiss", command=game_window.destroy).grid(row=1, column=0)

    def play_and_refresh(self, row, col):
        try:
            self._game.play(row+1, col+1)
        except GameError as e:
            print(e)

        text = self._game.at(row+1, col+1)
        self._buttons[row][col].set(text)

    def help_callback(self):
        pass

    def run(self):
        self._root.mainloop()

class Terminal(Ui):
    def __init__(self):
        self._game = Game()
    
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
