while True:
    a= int(input("a? "))
    b= int(input("b? "))
    op= input("operator?(+.-.*,/) ")
    if op == "+":
        print(a+b)
    elif op =="-":
        print(a-b)
    elif op == "*":
        print(a*b)
    elif op == "/":
        if b ==0:
            print("b != 0 please!!")
        else:
            print(a/b)       
    else:
        print("syntax error")

