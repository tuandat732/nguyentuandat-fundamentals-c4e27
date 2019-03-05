from math import *
a=int(input("nhap a:"))
b=int(input("nhap b:"))
c=int(input("nhap c:"))
if(a==0):
    if(b==0):
        if(c==0):
            print('pt vo so nghiem')
        else: print('pt vo nghiem')
    else:
        print('pt co nghiem duy nhat',-c/b)
else:
    delta=b*b-4*a*c
    m=-b/(2*a)
    k=sqrt(abs(delta))/(2*a)
    if(delta==0): print('pt co nghiem duy nhat',-b/(2*a))
    elif(delta>0):
        print("x1: ",m+k,"x2: ",m-k)
    else:
        m=-b/(2*a)
        k=sqrt(abs(delta))/(2*a)
        print("pt co nghiem phuc","\nx1= ",m,"+",k,"i\nx2= ",m,"-",k,"i")

