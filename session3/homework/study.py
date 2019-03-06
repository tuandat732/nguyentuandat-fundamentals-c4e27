# #1
# Danh sách lồng nhau là danh sách xuất hiện dưới dạng một thành phần trong danh sách khác.
# Để trích xuất một phần tử từ danh sách lồng nhau, chúng ta có thể tiến hành theo hai bước.
# Đầu tiên, trích xuất danh sách lồng nhau, sau đó trích xuất mục quan tâm.
# Cũng có thể kết hợp các bước đó bằng cách sử dụng các toán tử khung đánh giá từ trái sang phải.
b=[[1,2,3],[3,4,5],[5,6,7]]
#c1
a=b[2]
print(a[1])
#c2
print(b[2][1])
for i in range(len(b)):
    print(b[i])
# #2
# trong list có thể dùng cả str và int
a=['dat',1,'tram',5,6]
print(a)