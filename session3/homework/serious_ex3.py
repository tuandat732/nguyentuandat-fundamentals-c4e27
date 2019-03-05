from random import *
a=['decade','kuuga','ryuki','exaid','ghost','agito','faiz','ghost','blade','kiva','wizard']
b=a.copy()
for i in range(len(a)):
    n=list(a[i])
    shuffle(n)
    print(*n)
    m=input("nhap cau tl(neu chan thi nhap exit): ")
    if(m=='exit'): break
    elif(a[i]==m):
        print("hura")
    else: print("ngu bo")
