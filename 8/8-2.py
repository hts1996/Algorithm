M=int(input())
N=int(input())
list_num=list(range(M,N+1))
a=[]
for i in list_num:
    cnt=0
    if i == 1:
        pass
    else:
        for j in range(2,i+1):
            if i%j == 0 and i!=j:
                cnt+=1
            
        if cnt == 0:
            a.append(i)
if len(a) == 0:
    print(-1)
else:
    print(sum(a))
    print(min(a))