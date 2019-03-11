from turtle import *
speed(0)
#1
def say():
    for i in range(3):
        print("hello world")


#2
def tong(a,b):
    print("tong a,b: ",a+b)


#3,4
def draw_square(length,color1):
    color(color1)
    for i in range(4):
        forward(length)
        left(90)

for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
# mainloop()

#5
def draw_star(x,y,z):
    penup()
    goto(x,y)
    pendown()
    for i in range(5):
        forward(z)
        right(144)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
mainloop()
