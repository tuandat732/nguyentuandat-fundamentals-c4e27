from turtle import *
speed(0)
mau=['red', 'blue', 'brown', 'yellow', 'grey']
goc=[120,90,72,60,51.5]
for i in  range(5):
    color(mau[i])
    for j in range(i+3):
        forward(100)
        left(goc[i])
penup()
forward(300)
pendown()
s=[50,100,50,100]
for i in range(5):
        color(mau[i])
        begin_fill()
        for j in range(4):
                forward(s[j])
                left(90)
        end_fill()
        forward(50)
mainloop()
