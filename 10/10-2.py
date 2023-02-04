sum=0
list_num=[]
for i in range(5):
    num=int(input())
    sum+=num
    list_num.append(num)

print(int(sum/5))
print(sorted(list_num)[2])
    