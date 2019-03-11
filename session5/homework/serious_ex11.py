from math import *
def is_inside(a,b):
    dem=0
    for i in range(2):
        if  abs(b[i])<=abs(a[i])<=abs(b[i])+b[i+2]:
            dem+=1
    if(dem==2): return True
    return False
    
if(is_inside([200, 120], [140, 60,100,200])):
    print("Your function is correct")
else:
    print("Oops, there's a bug")