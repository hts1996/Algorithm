import sys
T,n=map(int,sys.stdin.readline().split())
num_list=list(map(int,sys.stdin.readline().split()))
a=[]
for i in range(T):
    for j in range(i+1,T):
        for k in range(j+1,T):
            sum=num_list[i]+num_list[j]+num_list[k]
            a.append(sum)
min=abs(n-a[0])
for l in a:
    if abs(n-l)<min and l<=n:
        min=abs(n-l)
        cnt=l
print(cnt)