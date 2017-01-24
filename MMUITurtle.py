from turtle import Turtle, Screen


class MMUITurtle:
    def __init__(self):
        self.tt = Turtle()
        self.screen = Screen()
        self.board = None
        self.pincolorSize = 11
        self.currentLine = []
        self.pincolorTable =   [((-34, -173), (2, -173),  (37, -172), (72, -173)),   #First line from bottom
                                ((-34, -132), (-1, -132), (37, -132), (72, -132)),   #Second line from bottom
                                ((-34, -93),  (2, -93),   (37, -93),  (72, -93)),
                                ((-34, -53),  (2, -53),   (37, -53),  (72, -53)),
                                ((-34, -13),  (1, -13),   (37, -13),  (72, -13)),
                                ((-34, 27),   (2, 27),    (37, 27),   (72, 27)),
                                ((-34, 67),   (2, 67),    (37, 67),   (72, 67)),
                                ((-34, 107),  (2, 107),   (37, 107),  (72, 107))]

    def display(self):
        self.tt.hideturtle()
        self.screen.bgpic("./data/mm_board.gif")
        self.screen.onclick(self.onclick)
        self.screen.mainloop()

    def drawcircle(self, pos, color, size):
        self.tt.up()
        self.tt.setpos(pos)
        self.tt.down()
        self.tt.color(color)
        self.tt.begin_fill()
        self.tt.circle(size)
        self.tt.end_fill()

    def onclick(self, x, y):
        print("MMUITurtle: ", x, y)
        line = self.board.getcurrentrow()
        print("Position on board: ", line, len(self.currentLine))

        color = "green"
        self.drawcircle(self.pincolorTable[line][len(self.currentLine)], color, self.pincolorSize)
        self.currentLine.append(color)
        if len(self.currentLine) == 4:
            self.board.addRow(color)
            self.currentLine = []

    def setboard(self, board):
        self.board = board
