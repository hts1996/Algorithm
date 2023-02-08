num=str(input())
for i in range(int(num)):
    list_num=list(map(int,str(i)))
    a=i+sum(list_num)
    if a == int(num):
        print(i)
        break
    if i == int(num)-1:
        print(0)
        break