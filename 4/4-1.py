size=int(input())
list_num=list(map(int,input().split()))
num=int(input())
counting=0
for i in range(len(list_num)):
    if list_num[i]==num:
        counting+=1
print(counting)