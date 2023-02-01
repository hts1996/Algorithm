list_num=[]
list_1=[]
for i in range(10):
    a=str(input())
    list_num.append(a)
for j in range(len(list_num)):
    list_1.append(str(int(list_num[j])%42))
list_2=set(list_1)
print(len(list_2))