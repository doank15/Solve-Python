import collections

test = int(input())
shoes = collections.Counter(map(int, input().split()))  # convert 1 list from string to int using map function
#collections.Counter(): count so lan xuat hien cua 1 cap key and value
numOfTest=int(input())

sumPrice=0

for x in range(numOfTest):
    size, price=map(int, input().split())  # nhu nhap 1 list 
    if shoes[size]:
        sumPrice+=price
        shoes[size]-=1

print(sumPrice)