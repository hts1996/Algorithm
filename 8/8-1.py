num=int(input())
num_list=list(map(int,input().split()))
for i in num:
    if i == 1:
        num_list.remove(i)
    else:
        for j in range(len(num_list)):
            if num_list[j]%i == 0:
                num_list.remove(i)
print(num_list)
