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

x=['BLUE','RED','YELLOW','GREEN']
y=['#3F51B5','#C62828','#FFD600','#4CAF50']
def generate_quiz():
    m=choice(x)
    n=choice(y)
    z=randint(0,1)
    return [
                m,
                n,
                z # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    for i in range(4):
        text=text.lower()
        if (color==shapes[i]['color'] and quiz_type==1) or (text==shapes[i]['text'] and quiz_type==0):
            if(shapes[i]['rect'][0]<=x<=shapes[i]['rect'][0]+shapes[i]['rect'][2] and shapes[i]['rect'][1]<=y<=shapes[i]['rect'][1]+shapes[i]['rect'][3]):
                return True
            else: return False






    
    
