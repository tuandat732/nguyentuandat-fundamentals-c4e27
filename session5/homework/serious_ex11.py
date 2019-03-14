from random import *
def is_inside(a,b):
    dem=0
    for i in range(2):
        if  b[i]<=a[i]<=b[i]+b[i+2]:
            dem+=1
    if(dem==2): return True
    return False
    
for i in range(10):
    m=randrange(0,300)
    k=randrange(0,300)
    if(is_inside([m,k],[140, 60, 100, 200])):
        print('toa do %d %d trong hinh chu nhat' %(m,k))
    else:
        print("toa do %d %d ko trong hinh" %(m,k))