
câu 1:
khi dùng hàm, mỗi hàm có thể dùng đi dùng lại nhiều lần mà k cần phải viết lại đoạn code nào nx khi dùng các lệnh khác
từ đó đoạn code sẽ ngắn gọn hơn và dễ hiểu hơn. 
khi dùng hàm , mỗi khi cần dùng đến chỉ cần nêu lại tên hàm và tùy vào mục đích sử dụng khác nhau để định nghĩa hàm

câu 2:
cú pháp:
    def <tên hàm>(tham số truyền vào(có thể có or ko)):
        khối lệnh

câu 3:
cú pháp gọi tên hàm:
    <tên hàm>(tham số truyền vào)

câu 4:
return dùng để trả lại 1 hay nhiều giá trị của 1 hàm
khi kết thúc hàm, giá trị của nó sẽ biến mất luôn nếu k dùng lệnh return 
chình vì thế để dùng lại giá trị đó thì cần dùng return
*cú pháp:
def <tên hàm>(tham số truyền vào):
        khối lệnh
        return <giá trị cần trả lại>


câu 5:
không. chỉ dùng return khi cần trả lại giá trị của hàm
vd:
    def say_hi():
        print('hi')
say_hi()
    khi đó màn hình sẽ in ra 'hi' 

câu  6:
tham số của hàm là giá trị mà hàm cần dùng để xử lý các tác vụ trong hàm (có thể là lệnh print hoặc return)
def <tên hàm>(a,b):
    câu lệnh
    trong đó a, blà các tham số cần dùng

câu 7: 
để dùng các hàm ở các tệp khác, ta sẽ phải truy suất tên tệp chứa 1 hoặc nhiều hàm cần dùng
*cú pháp:
    import <tên tệp chứa hàm>
    <tên tệp chứa hàm>.func()
hoặc
    from <tên tệp chứa hàm> import <hàm>
    <hàm>