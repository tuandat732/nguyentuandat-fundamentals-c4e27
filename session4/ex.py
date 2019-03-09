a=[]
n=int(input("nhap n: "))
for i in range(n):
    m=int(input("nhap cac so: "x))
    a.append(m)
for i in range(n):
    for j in range(i+1,n):
        if((a[i]+a[j])%2==0): print (a[i],a[j])
