import pandas as pd
import HandTrackingModule as hm

def User(Ten):
    "Mo ta ngan ve ham" #khong bat buoc
    print("Hello! " + Ten.title())
    return;
name="Mai The Doan"
User(name) #goi ham
'''
Ham chua nhieu tham so 
'''
def User(a,b,c):
    "Ham tra ve tong 3 so"
    print("Tong 3 so la:")
    return a+b+c
#*
x=1
y=2
z=3
print(User(x,y,z))  

'''
Ham co so luong tham so co the thay doi duoc
above( phan: *) 
'''
def Sum(*a):
    sum=0
    for so in a:
        sum+=so
    print(sum)

x1,x2,x3=10,20,30
Sum(10,20,30) #-->  ans = 60

#ham co gia tri tra ve
def User(Ho, Ten):
    Ho_va_Ten=Ho+ " "+Ten
    return Ho_va_Ten.title()

ho="Mai"
ten="Doan"
print( User(ho,ten))


#chuong trinh tinh giai thua 1 so nhap tu ban phim 

def Factorial(x):
    if x==0 or x==1:
        return 1;
    return x*Factorial(x-1)

n=int(input())
print(Factorial(n))