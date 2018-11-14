# def add(a,b):               #a,b; function argument
#     r= a+b
#     return r
# #call function
# s =add(3,4)
# print(s)
from random import *
def eval(a,op,b):
    if op == "+":
        r = a + b
    elif op == "-":
        r = a - b
    elif op == "*":
        r = a*b
    elif op == "/":
        r = a/b
    else:
        r = "op not supported"
    return r
def gen_quiz():
    op_list = [ "+","-","*","/"]
    a= randint(1,11)
    b= randint(1,11)
    op = choice(op_list)
    error= randint(-2,2)
    r = eval(a,op,b) + error
    return a,op,b,r,error
gen_quiz()