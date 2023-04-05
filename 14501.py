import sys
from collections import deque
n=int(sys.stdin.readline())
t=[0]*(n+2)
p=[0]*(n+2)
for i in range(1,n+1):
    a,b=map(int,sys.stdin.readline().split())
    p[i]=b
    t[i]=a
v=[0]*(n+1)
queue=deque()
queue.append((1,0))
MAX=0
while queue:
    s,ans=queue.popleft()
    if ans>MAX:
        MAX=ans
    if s == n+1:
        continue
    if s+1 < n + 1:
        queue.append((s+1,ans))
    ans+=p[s]
    s+=t[s]

    if s<=n+1:
        queue.append((s,ans))
print(MAX)