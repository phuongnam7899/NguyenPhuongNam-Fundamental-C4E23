from random import *
from function import eval

def generate_quiz():
    op_list = [ "+","-","*","/"]
    x= randint(1,11)
    y= randint(1,11)
    op = choice(op_list)
    error= randint(-1,1)
    result = eval(x,op,y) + error
    return [x,y,op,result]
    # Hint: Return [x, y, op, result]
    # return [0, 0, '@@', 12]

def check_answer(x, y, op,result, user_choice):
    if user_choice == True:
        if eval(x,op,y) == result:
            return True
        else:
            return False

    elif user_choice == False:
        if eval(x,op,y) != result:
            return True
        else:
            return False
          
    
