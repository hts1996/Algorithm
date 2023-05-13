import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
def dfs(s):
    for i in tree[s]:
        if v[i]!=0:
            pass
        else:
            v[i]=s
            dfs(i)
n = int(input())
tree=[[]for _ in range(n+1)]
for _ in range(n-1):
    L=list(map(int,input().split()))
    L.sort()
    tree[L[0]].append(L[1])
    tree[L[1]].append(L[0])
v=[0 for _ in range(n+1)]
v[1]=1
dfs(1)
for i in range(2,n+1):
    print(v[i])
