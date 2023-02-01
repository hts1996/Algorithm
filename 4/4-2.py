a,b=map(int,input().split())
list_num=list(map(int,input().split()))
list_1=list()
for i in range(len(list_num)):
    if list_num[i]<b:
        list_1.append(list_num[i])
print(*list_1)