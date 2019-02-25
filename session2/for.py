#chuỗi có thể hiểu là 1 mảng các kí tự
#vòng for trong python bắt đầu từ 0
#tham số trong vòng lặp phải là số nguyên
#<stop
#step ko dc la so 0,mặc định là 1
#tham số stop bắt buộc có còn step và start ko bắt buộc

# for i in 'hello':
#     print(i,end=' ') run h e l l o
# print(range(10)) run ra range(0,10)
# print(list(range(10))) run ra [0,1,2,3,4,..9]

# for i in range(10):
#     y=3*i*i+2*i+1
#     print(i)
#tinh tong day tu 1 den 10
tong=0
tong1=0
for i in range(1,11):
    tong=tong+i
    tong1=tong1+i*i
print(tong)
print(tong1)
