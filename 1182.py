import sys
def dfs(s,e,N):
    global cnt, SUM
    if SUM == m and N!=0:
        cnt+=1
        return
    for i in range(e,n):
        if v[i] == 0:
            v[i] =1
            SUM+=num[i]
            dfs(s+1,i,N+1)
            v[i] = 0
            SUM -= num[i]
n,m=map(int,sys.stdin.readline().split())
num=list(map(int,sys.stdin.readline().split()))
v=[0]*n
SUM=0
cnt=0
dfs(0,0,0)
print(cnt)