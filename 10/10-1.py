num=int(input())
list_1=[]
for i in range(num):
    list_1.append(int(input()))
mod_list=sorted(list_1)
for j in range(len(mod_list)):
    print(mod_list[j],end="\n")