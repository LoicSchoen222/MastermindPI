import os
from turtle import Turtle, Screen

cc = Turtle()
screen = Screen()

screen.bgpic("./data/mm_board.gif")

pinColorTable = [((-34, -173), (2, -173), (37, -172), (72, -173)),
            ((-34, -132), (-1, -132), (37, -132), (72, -132)),
            ((-34, -93), (2, -93), (37, -93), (72, -93)),
            ((-34, -53), (2, -53), (37, -53), (72, -53)),
            ((-34, -13), (1, -13), (37, -13), (72, -13)),
            ((-34, 27), (2, 27), (37, 27), (72, 27)),
            ((-34, 67), (2, 67), (37, 67), (72, 67)),
            ((-34, 107), (2, 107), (37, 107), (72, 107))]

pinResultTable = [((-83, -173), (-69, -173), (), ()),
                  ((), (), (), ())]

def f(x, y):
    print(x, y)

def drawcircle(pos, color, size):
    cc.up()
    cc.setpos(pos)
    cc.down()
    cc.color(color)
    cc.begin_fill()
    cc.circle(size)
    cc.end_fill()
    
cc.hideturtle()
drawcircle(pinColorTable[0][0], "green", 10)
#drawcircle(-83, -173, "red", 4)
#drawcircle(-69, -173, "red", 4)
#drawcircle(-83, -159, "white", 4)
#drawcircle(-69, -159, "white", 4)
#drawcircle(-82, -133, "red", 4)
#drawcircle(-68, -133, "red", 4)
#drawcircle(-83, -120, "red", 4)
#drawcircle(-69, -120, "red", 4)

screen.onclick(f)
screen.mainloop()

print("done")
