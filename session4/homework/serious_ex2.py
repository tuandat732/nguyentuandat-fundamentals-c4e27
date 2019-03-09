prices={"banana": 4,"apple": 2,"orange": 1.5,"pear": 3}
stock={"banana": 6,"apple": 0,"orange": 32,"pear": 15}
tong=0
for i in prices.keys():
    print(i)
    print("price:",prices[i])
    print("stock:",stock[i])
print()
for i,j in prices.items():
    print(i,j*stock[i])
    tong=tong+j*stock[i]
print("\ntien kiem dc neu ban het la: ",tong)



 
  
    