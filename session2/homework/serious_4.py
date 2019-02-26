print("câu a")
for i in range(20): print("*",end=' ')
print()

print("câu b")
n=int(input("nhap n: "))
for i in range(n): print("*",end=' ')
print()

print("câu c")
for i in range(9):
    if(i%2==0): print("x",end=' ')
    else: print("*",end=' ')
print()

print("câu d")
m=int(input("nhap m: "))
for i in range(m):
    if(i%2==0): print("x",end=' ')
    else: print("*",end=' ')

#e
print()

print("câu f")
for i in range(3):
    for j in range(7):
        print("*",end=' ')
    print()   

print("câu g")
b=int(input("nhap n: "))
c=int(input("nhap m: "))
for i in range(c):
    for j in range(b):
        print("*",end=' ')
    print()        