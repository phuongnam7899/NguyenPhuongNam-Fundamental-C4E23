from ex_1_2 import draw_square
from turtle import *
speed(0)
for i in range(30):
    draw_square(i * 5, "red")
    left(17)
    penup()
    forward(i * 2)
    pendown()
mainloop()
