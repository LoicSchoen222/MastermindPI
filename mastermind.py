import MMBoard
import MMUITurtle


class Mastermind:
    def __init__(self):
        self.board = MMBoard.MMBoard()
        self.board.setFinalRow(("gray", "green", "yellow", "pink"))
        self.ui = MMUITurtle.MMUITurtle()
        self.ui.setboard(self.board)

    def start(self):
        self.ui.display()


if __name__ == '__main__':
    mm = Mastermind()

    # Start to play!
    mm.start()
