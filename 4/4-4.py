list_num=[]
for i in range(9):
    a=str(input())
    list_num.append(a)
max=int(list_num[0])
for j in range(9):
    if int(list_num[j])>=max:
        max=int(list_num[j])
        n=j+1
    else:
        pass
print(f'{max}\n{n}')