import sys
n,T,p=map(int,sys.stdin.readline().split())
if n!=0:
    score=list(map(int,sys.stdin.readline().split()))
    cnt=1
    ans=1
    for i in range(n):
        if score[i]>=T:
            cnt+=1
        if score[i]>T:
            ans+=1
        if cnt>p:
            ans=-1
else:
    ans=1
print(ans)
