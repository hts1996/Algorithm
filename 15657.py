def dfs(s):
    global ans
    if s == m:
        for j in range(m-1):
            if ans[j]>ans[j+1]:
                return
        print(*ans)
        return
    for i in range(n):
        ans.append(num[i])
        dfs(s + 1)
        ans.pop()
n,m=map(int,input().split())
num=list(map(int,input().split()))
num.sort()
ans=[]
v=[0 for _ in range(n)]
dfs(0)
