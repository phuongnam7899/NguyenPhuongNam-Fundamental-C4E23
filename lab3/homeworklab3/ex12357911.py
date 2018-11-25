from turtle import *
#1
def hlw_x3():
    for i in range(3):
        print("hello world")
#2
def print_sum(a,b):
        s = a + b
        print(s)
#3
def draw_square(length,colors):
        color(colors)
        for k in range(4) :
                forward(length)
                left(90)
#5
def draw_star(x,y,length):
        penup()
        setx(x)
        sety(y)
        pendown()
        for i in range(5):          
                forward(length)
                right(144)
#7
def remove_dollar_sign(s):
        new_s = s.replace("$","")
        return new_s
#9
def get_even_list(l):
        even_list=[]
        for number in l:
                if (number%2) == 0 :
                        even_list.append(number)
        return(even_list)
#11
def is_insight(l1,l2):
        if (l1[0]>l2[0]) and (l1[0]<l2[0]+l2[2]) and (l1[1]>l2[1]) and (l1[1]<l2[1]+l2[3]) :
                return True
        else:
                return False

                

