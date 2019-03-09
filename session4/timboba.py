for i in range(101):
    for j in range(101):
        for k in range(101):
            if(i*i+j*j+k*k==i*k*j):
                print(i,j,k)