import sys
def dfs(dele):
    for i in dele:
        if len(tree[i])==0:
            tree[i]=[-1]
        else:
            dfs(tree[i])
n=int(sys.stdin.readline())
tree=[[]for _ in range(n)]
L=list(map(int,sys.stdin.readline().split()))
a=int(sys.stdin.readline())
for i in range(len(L)):
    if L[i] == -1:
        pass
    else:
        tree[L[i]].append(i)

dele=tree[a]
tree[a]=[-1]
dfs(dele)
cnt=0
for i in range(n):
    if a in tree[i]:
        tree[i].remove(a)
for i in range(len(tree)):
    if len(tree[i])==0:
        cnt+=1
print(cnt)