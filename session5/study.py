# a=[]
# b=[]
# n=int(input("nhap n:"))
# for i in range(n):
#     m=int(input("nhap so:"))
#     a.append(m)
# print('tong day vua nhap la',sum(a))
# m=int(input("nhap so m:"))
# for i in range(m):
#     k=int(input("nhap so:"))
#     b.append(k)
# print('trung binh cong day vua nhap la:',sum(b)/m)

# def tong(a,b):
#     return a+b
# a=int(input("nhap: "))    
# b=int(input("nhap: "))  
# c=int(input("nhap: "))  
# tong1=tong(a,b)
# tong2=tong(tong1,c)
# print(tong2)

# def abss(a):
#     if(a<0):
#         return -a
#         print("tri tuyet doi la",-a) //neu a am thi se return ve -a va ko thuc hien cac cau lenh sau
#     else:
#         return a
#         print("tri tuyet doi la",a)
#     print("tri tuyetj doi la",a)
# x= abss(0)
# tong=12+abss(-12)
# print(x,tong)

# def evaluate(a,b,x):
#     if(x=='+'): return a+b
#     elif(x=='*'): return a*b
#     elif(x=='-'): return a-b
#     elif(x=='/' and b!=0): return a/b
#     elif(x=='%' and b!=0): return a%b
#     else: 
#         return 'nhap sai phep toan hoac ko tinh dc'
# a=int(input("nhap so a:"))
# b=int(input("nhap so b:"))
# c=str(input("nhap phep tinh:"))
# print(evaluate(a,b,c))

#kt so nguyen to
#cach 1: dung ham
# from math import *
# def ktsonguyento(n):
#     if(n<2): return 0
#     for i in range(2,int(sqrt(n))+1):
#         if(n%i==0): return 0
#     return 1
# n=int(input("nhap n:"))
# for i in range(n):
#     if(ktsonguyento(i)==1):
#         print(i,end=' ')

#cach 2(sang ngto)
b=[]
n=int(input("nhap n:"))
for i in range(n):
    b.append(0)
for i in range(2,n):
    if(b[i]==0):
        print(i,end=' ')
        for j in range(i,n,i):
            b[j]=1
        
        

    
        






