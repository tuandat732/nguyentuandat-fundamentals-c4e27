from random import *
x=0
quiz={'if x=k, then what is the value of 4(x+3)':[]}
for i,j in quiz.items():
    k=randrange(30)
    print(i,'(k = %d)'%k)
    for l in range(3):
        m=randrange(30)
        quiz[i].append(4*(3+m))
    quiz[i].append(4*(k+3))
    shuffle(j)
    for i in range(len(j)):
        print(i+1,j[i],sep='.')
    chon=int(input("your choice:"))
    if(j[chon-1]==4*(3+k)): print ("bingo")
    else: print("ngu vll")
  
    
   






        