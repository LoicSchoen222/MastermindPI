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

pinResultTable = [((-83, -173), (-69, -173), (-83, -159), (-69, -159)),
                  ((-82, -133), (-68, -133), (-83, -120), (-69, -120)),
                  ((-83, -94),  (-69, -94),  (-83, -80),  (-68, -80)),
                  ((-82, -53),  (-68, -53),  (-82, -40),  (-69, -40)),
                  ((-83, -14),  (-68, -14),  (-83, -0),   (-68, -0)),
                  ((-83, 26),   (-68, 26),   (-83, 40),   (-68, 40)),
                  ((-83, 66),   (-68, 66),   (-83, 80),   (-68, 80)),
                  ((-83, 106),  (-68, 106),  (-83, 120),  (-68, 120))]


def circleclick(poso, post, color):
    cc.up()
    cc.setpos(poso, post)
    cc.down()
    cc.color("black", color)
    cc.begin_fill()
    cc.circle(20)
    cc.end_fill()
    
def getcolor(x, y):
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
    return "no color"


                  
def f(x, y):
    color = getcolor(x, y)
    print(color)

def drawcircle(pos, color, size):
    cc.up()
    cc.setpos(pos)
    cc.down()
    cc.color(color)
    cc.begin_fill()
    cc.circle(size)
    cc.end_fill()
    
    


cc.hideturtle()
circleclick(-163, -303, "pink")
circleclick(-113, -303, "white")
circleclick(-63, -303, "red")
circleclick(-13, -303, "yellow")
circleclick(43, -303, "orange")
circleclick(93, -303, "green")
circleclick(143, -303, "blue")
circleclick(193, -303, "gray")




#for i in range(8):
 #   for t in range(4):
  #      drawcircle(pinColorTable[i][t], "white", 10)

#for i in range(8):
 #   for t in range(4):
  #      drawcircle(pinResultTable[i][t], "red", 5)

screen.onclick(f)
screen.mainloop()

print("done")
