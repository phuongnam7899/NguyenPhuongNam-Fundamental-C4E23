from random import *
import function
op_list = [ "+","-","*","/"]
point = 0
while True:
    a,op,b,r,error = function.gen_quiz()
    print(a,op,b,'=',r)
    ans = input("t/f? ")
    if ans == "t":
        if error==0:
            print("true")
            point += 1
        else:
            print("wrong")
            break
    if ans == "f":
        if error != 0:
            print("true")
            point += 1
        else:
            print("wrong")
            break
print("your point: ",point)
    