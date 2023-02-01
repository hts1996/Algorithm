num=int(input())
list_num=list(map(int,input().split()))
max=list_num[0]
min=list_num[0]
for i in range(num):
    if list_num[i]>=max:
        max=list_num[i]
    if list_num[i]<=min:
        min=list_num[i]
print(min,max)
