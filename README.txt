====Text Alignment=====
+Trong python 1 chuỗi có thể được căn chỉnh nhờ thuộc tính:
        -ljust(width) :căn trái
        -center(width):căn giữa 
        -rjust(width): căn phải 

+Đếm số lần xuất hiện của 1 giá  trị trong 1 danh sách 
        -collections.Counter(map(int, input().split()))



+Bài String Validators trong solve python 
        -dùng thuộc tính any để print nếu chuỗi có bất kì 1 cái j đó 
        -bài mẫu 
        /*
        s = input()
        print(any(a.isalnum() for a in s) )
        print(any(a.isalpha() for a in s) )
        print(any(a.isdigit() for a in s) )
        print(any(a.islower() for a in s) )
        print(any(a.isupper() for a in s) )
        */
        