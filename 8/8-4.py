M,N=map(int,input().split())
num_list=list(range(M,N+1))
a=num_list[::]
for i in range(2,N+1):
    for j in num_list:
        if j%i==0 and i!=j:
            a.remove(j)
    num_list=a
for k in a:
    if k>=M:
        print(k)