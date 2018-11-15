from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]


def get_shapes():

    return shapes

def generate_quiz():
    text_list = []
    color_list= []
    for shape in shapes:
        text_list.append(shape["text"])
        color_list.append(shape["color"])
    color = choice(color_list)
    quiz_type = randint(0, 1)
    if quiz_type == 0:
        text= choice(text_list) + "(meaning)"
    elif quiz_type == 1:
        text= choice(text_list) + "(color)"
    return [    text,
                color,
                quiz_type # 0 : meaning, 1: color
            ]

def is_insight(l1,l2):
        if (l1[0]>l2[0]) and (l1[0]<l2[0]+l2[2]) and (l1[1]>l2[1]) and (l1[1]<l2[1]+l2[3]) :
                return True
        else:
                return False

def mouse_press(x, y, text, color, quiz_type):
    for shape in shapes:
        if is_insight([x,y],shape["rect"]) == True:
            shape_choosed =  shape
    if quiz_type == 0:
        if text == shape_choosed["text"] + "(meaning)":
            return True
        else:
            return False
    else:
        if color == shape_choosed["color"]:
            return True
        else:
            return False

            
