nhap = input("nhập 1 câu đê: ")
nhap = nhap.lower() 
bangchucai = 'abcdefghijklmnopqrstuvwxyz'
dem = {} 
for i in nhap:
    if i in bangchucai: 
        if i in dem: dem[i]+=1
        else: dem[i] = 1
dem=dem.items()
for i,k in sorted(dem):
    print(i,k)