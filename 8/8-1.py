num=int(input())
num_list=list(map(int,input().split()))
m=num
for i in num_list:
    n=0
    if i == 1:
        m-=1
    else:
        for j in range(2, i+1):
            if i % j == 0 and j != i:
                n+=1
            else:
                pass
            i
        if n>0:
            m-=1
print(m)
