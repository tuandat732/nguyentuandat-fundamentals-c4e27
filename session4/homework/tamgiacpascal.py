#cach 1
# def giatri(k,n):
#     if(k==0 or k==n): 
#         return 1
#     elif(k==1): 
#         return n
#     return giatri(k-1,n-1) + giatri(k,n-1)

# m=int(input("nhap n: "))
# for i in range(m):
#     for j in range(i+1):
#         print(giatri(j,i),end=' ')
#     print()

#cach 2
n=int(input("nhap n: "))
a=[[] for _ in range(n)]
for i in range(n):
    for j in range(i+1):
        if(j==0 or j==i):
            a[i].append(1)
        else:
            k=(a[i-1][j-1]+a[i-1][j])
            a[i].append(k)
for i in range(n):
    for j in range(i+1):
        print(a[i][j],end=' ')
    print()          



    