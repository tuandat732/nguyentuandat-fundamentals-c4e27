n=int(input("nhap n:"))
ls=[]
for i in range(n):
    print("nhap gia tri thu",i+1)
    so=int(input())
    ls.append(so)
print("day vua nhap",ls)
print("tong day",sum(ls))

#them phan tu vao mang append()
#xoa pt khoi mang remove(...) //... la ten gia tri cua pt


# for i in range(n):
#     tong=tong+a[i]
#     if(a[i]%2!=0): tongle=tongle+a[i]
#     else:
#         tongchan=tongchan+a[i]
#         dem+=1

