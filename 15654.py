def dfs(s):
    global ans
    if s == m:
        print(*ans)
        return
    for i in range(n):
        if v[i] == 0:
            v[i]=1
            ans.append(num[i])
            dfs(s + 1)
            ans.pop()
            v[i]=0
n,m=map(int,input().split())
num=list(map(int,input().split()))
num.sort()
ans=[]
v=[0 for _ in range(n)]
dfs(0)