#1 bool
# kiểu bool là kiểu dữ liệu chỉ nhận 2 giá trị true hoặc false
# ví dụ
print(2==6)

a='nguyentuandat'
print('a' in a)
print('m' in a)

a=[1,2,3]
b=a[:]
c=a
print(b is a)
print(c is a)

#2
# lưu đồ là một loại sơ đồ biểu diễn một thuật toán hoặc 1 quá trình,
# biểu hiện qua các bước công việc dưới dạng các loại hình hộp khách
# nhau theo thứ tự được biểu diễn bởi các mũi tên. sơ đồ này có thể 
# hiện phương pháp giait cho 1 vấn đề cần giải quyết theo từng bước 1


#3
# điều kiện lồng nhau: là khối lệnh gồm các câu lệnh if,else,elif và 
# trong các câu lệnh điều kiện đó còn các câu lệnh khác
# ví dụ
n= int(input("nhap n: "))
if(n>2):
    if(n%5==0): print("true")
    else: print("false")
else: print("false")