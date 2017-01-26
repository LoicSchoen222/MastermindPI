from turtle import Turtle, Screen


class MMUITurtle:
    def __init__(self):
        self.tt = Turtle()
        self.screen = Screen()
        self.board = None
        self.pincolorSize = 11
        self.currentLine = []
        self.drawing = False
        self.pincolorTable =   [((-34, -173), (2, -173),  (37, -172), (72, -173)),   #First line from bottom
                                ((-34, -132), (-1, -132), (37, -132), (72, -132)),   #Second line from bottom
                                ((-34, -93),  (2, -93),   (37, -93),  (72, -93)),
                                ((-34, -53),  (2, -53),   (37, -53),  (72, -53)),
                                ((-34, -13),  (1, -13),   (37, -13),  (72, -13)),
                                ((-34, 27),   (2, 27),    (37, 27),   (72, 27)),
                                ((-34, 67),   (2, 67),    (37, 67),   (72, 67)),
                                ((-34, 107),  (2, 107),   (37, 107),  (72, 107))]
        self.pinResultTable =  [((-83, -173), (-69, -173), (-83, -159), (-69, -159)),
                                ((-82, -133), (-68, -133), (-83, -120), (-69, -120)),
                                ((-83, -94),  (-69, -94),  (-83, -80),  (-68, -80)),
                                ((-82, -53),  (-68, -53),  (-82, -40),  (-69, -40)),
                                ((-83, -14),  (-68, -14),  (-83, -0),   (-68, -0)),
                                ((-83, 26),   (-68, 26),   (-83, 40),   (-68, 40)),
                                ((-83, 66),   (-68, 66),   (-83, 80),   (-68, 80)),
                                ((-83, 106),  (-68, 106),  (-83, 120),  (-68, 120))]


    def circleclick(self, poso, post, color):
        self.tt.up()
        self.tt.setpos(poso, post)
        self.tt.down()
        self.tt.color("black", color)
        self.tt.begin_fill()
        self.tt.circle(20)
        self.tt.end_fill()

    def display(self):
        self.tt.hideturtle()
        self.screen.bgpic("./data/mm_board.gif")
        self.circleclick(-163, -303, "pink")
        self.circleclick(-113, -303, "white")
        self.circleclick(-63, -303, "red")
        self.circleclick(-13, -303, "yellow")
        self.circleclick(43, -303, "orange")
        self.circleclick(93, -303, "green")
        self.circleclick(143, -303, "blue")
        self.circleclick(193, -303, "gray")
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

    def drawpin(self, x, y):
        color = self.getcolor(x, y)
        if color != None:
            line = self.board.getcurrentrow()
            print("Position on board: ", line, len(self.currentLine))

            self.drawcircle(self.pincolorTable[line][len(self.currentLine)], color, self.pincolorSize)
            self.currentLine.append(color)
            if len(self.currentLine) == 4:
                self.board.addRow(self.currentLine)
                self.currentLine = []

    def getcolor(self, x, y):
        print("getcolor: ", x ,y)
        if x > -183 and x < -143 and y > -303 and y < -263:
            return "pink"
        elif x > -133 and x < -93 and y > -303 and y < -263:
            return "white"
        elif x > -83 and x < -43 and y > -303 and y < -263:
            return "red"
        elif x > -33 and x < 6 and y > -303 and y < -263:
            return "yellow"
        elif x > 23 and x < 63 and y > -303 and y < -263:
            return "orange"
        elif x > 73 and x < 113 and y > -303 and y < -263:
            return "green"
        elif x > 123 and x < 163 and y > -303 and y < -263:
            return "blue"
        elif x > 173 and x < 213 and y > -303 and y < -263:
            return "gray"
        return None

    def onclick(self, x, y):
        if self.drawing == False:
            self.drawing = True
            self.drawpin(x, y)
            self.drawing = False

    def setboard(self, board):
        self.board = board
