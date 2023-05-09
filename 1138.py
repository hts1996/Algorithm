import sys
n=int(sys.stdin.readline())
L=list(map(int,sys.stdin.readline().split()))
loc=[0 for _ in range(n)]
for i in range(n):
    if loc[L[i]]==0 and loc[:L[i]].count(0)==L[i]:
        loc[L[i]]=i+1
    else:
        a=L[i]
        while True:
            a+=1
            if loc[a]==0 and loc[:a].count(0)==L[i]:
                break
        loc[a]=i+1
print(*loc)
