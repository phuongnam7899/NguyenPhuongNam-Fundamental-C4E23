from random import *
point = 0
while True:
    a= randint(1,11)
    b= randint(1,11)
    c= randint((a+b-2),(a+b+2))
    print(a,"+",b,"=",c)
    ans = input("t/f? ")
    if ans == "t":
        if a + b == c:
            print("true")
            point += 1
        else:
            print('false')
            break
    elif ans == "f":
        if a + b == c:
            print("false")
            break
        else:
            print("true")
            point += 1
print("your point: ",point)