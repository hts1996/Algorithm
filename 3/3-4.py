bill=int(input())
num=int(input())
sum=0
for i in range(num):
    money,num1=map(int,input().split())
    sum+=money*num1
    if i == num-1:
        if sum==bill:
            print('Yes')
        else:
            print('No')