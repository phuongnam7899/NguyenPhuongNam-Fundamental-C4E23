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
    print()
    # Hint: Return [x, y, op, result]
    # return [0, 0, '@@', 12]

def check_answer(x, y, op,result, user_choice):
    if user_choice == True:
        if eval(x,op,y) == generate_quiz()[3]:
            return user_choice
        else:
            user_choice = False
            return user_choice

    else:
        if eval(x,op,y) == generate_quiz()[3]:
            return user_choice
        else:
            user_choice = True
            return user_choice
          
    
