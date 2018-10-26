from turtle import *
speed(100)
for i in range (3,7,1):
    if i%2==0:
        color("red")
    else:
        color("blue")
    for k in range (i):
        forward(200)
        left(360/i)
mainloop()