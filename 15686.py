import sys
from itertools import combinations
n,m=map(int,sys.stdin.readline().split())
chicken=[]
home=[]
i=0
for _ in range(n):
    road=list(map(int,sys.stdin.readline().split()))
    for j in range(n):
        if road[j] == 1:
            home.append((i, j))
        if road[j] == 2:
            chicken.append((i, j))
    i+=1
a=list(range(len(chicken)))
ans=0
ANS=[]
MINI=10000000
for c in combinations(chicken,m):
    ans=0
    for h in home:
        leng=1000000
        for j in range(m):
            leng=min(leng,abs(h[0]-c[j][0])+abs(h[1]-c[j][1]))
        ans+=leng
    MINI=min(MINI,ans)
print(MINI)
