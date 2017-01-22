import os
from turtle import Turtle, Screen

cc = Turtle()
screen = Screen()

screen.bgpic("./data/mm_board.gif")

def f(x, y):
    print(x, y)

screen.onclick(f)
cc.mainloop()

print("done")
