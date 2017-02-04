import MMBoard
import MMUITurtle
import random

class Mastermind:
    def __init__(self):
        self.board = MMBoard.MMBoard()
        choice = random.sample(["pink", "white", "red", "yellow", "orange", "green", "blue", "gray"], 4)
        #print(choice)
        self.board.setFinalRow(choice)
        #self.board.setFinalRow(("pink", "orange", "green", "gray"))
        self.ui = MMUITurtle.MMUITurtle()
        self.ui.setboard(self.board)

    def start(self):
        self.ui.display()


if __name__ == '__main__':
    mm = Mastermind()

    # Start to play!
    mm.start()

