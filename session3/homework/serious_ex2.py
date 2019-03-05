sizes=[5,7,300,90,24,50,75]
#2.1
print("hello, my name is Dat and these are my ship sizes\n",sizes)
#2.2
print("now my biggest sheep has size",max(sizes),"let's shear it")
#2.3
sizes[sizes.index(300)]=8
print("after shearing, here is my flock",sizes)
#2.4
for i in range(len(sizes)):
    sizes[i]=sizes[i]+50
print("one month has passed, now here is my flock",sizes)

#2.5
sizes2=[5,7,300,90,24,50,75]
print("hello, my name is Dat and these are my ship sizes\n",sizes2)
for i in range(1,4):
    print("MONTH",i)
    for j in range(len(sizes2)):
        sizes2[j]=sizes2[j]+50
    print("one month has passed, now here is my flock\n",sizes2)
    print("now my biggest sheep has size",max(sizes2),"let's shear it")
    sizes2[sizes2.index(max(sizes2))]=8
    print("after shearing, here is my flock\n",sizes2)

#2.6
sizes3=[5,7,300,90,24,50,75]
print("hello, my name is Dat and these are my ship sizes\n",sizes3)
for i in range(0,4):
    if(i>=1):
        print("MONTH",i)
        for j in range(len(sizes3)):
            sizes3[j]=sizes3[j]+50
        print("one month has passed, now here is my flock\n",sizes3)
    print("now my biggest sheep has size",max(sizes3),"let's shear it")
    if(i==3):
        print("my flock has size in total:",sum(sizes3))
        print("i would get",sum(sizes3),"* 2$ =",sum(sizes3)*2,"$")
    else:
        sizes3[sizes3.index(max(sizes3))]=8
        print("after shearing, here is my flock\n",sizes3)
        
        