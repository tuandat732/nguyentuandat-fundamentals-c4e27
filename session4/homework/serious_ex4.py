cauhoi={'if x=8, then what is the value of 4(x+3) ?':[ 35,36,40,44,44],'Jack scored these marks in 5 math tests: 49,81,72,66 and 52. what is the mean ?':['about 55','about 65','about 75','about 85','about 65']}
dem=0
for i in range(2):
    if(i==0): print("answer the following algebrea question:")
    else: print("estimate this answer(exact calculation not needed):")
for j,k in cauhoi.items():
    print(j)
    for m in range(len(k)-1):
        print(m+1,k[m],sep='.')
    chon=int(input("your choice: "))
    if(k[chon-1]==k[4]):
        print('bingo')
        dem+=1
    else: print('ngu vll')
print('you corecttly answer',dem,'of 2 questions')



