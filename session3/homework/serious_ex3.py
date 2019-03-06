from random import *
a=['decade','kuuga','ryuki','exaid','ghost','agito','faiz','ghost','blade','kiva','wizard']
b=a.copy()
print("fan kamen rider auto win")
for i in range(len(a)):
    n=list(a[i])
    shuffle(n)
    print(*n)
    m=input("nhập câu tl(nếu chán nhập exit): ")
    if(m=='exit'): break
    elif(a[i]==m):
        print("chuẩn fan r")
    else: print("ngu bò")
        
        
