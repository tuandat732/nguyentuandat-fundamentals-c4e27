#bai 1
from turtle import *
speed(0)
color("red")
right(30)
for i in range(4):
    for j in range(4):
        forward(50)
        if(j%2!=0): left(120)
        else: left(60)
    right(270)

penup()
goto(180,-60)
left(30)
pendown()

#bai 2
mau=["blue","red","blue","red"]
goc=[120,90,72,60]   
for i in range(4):
    color(mau[i])
    for j in range(1,i+4):
        forward(100)
        left(goc[i])   

mainloop()   