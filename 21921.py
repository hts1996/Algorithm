import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
visit=list(map(int,sys.stdin.readline().split()))
ans=sum(deque(visit[:m]))
MAX=ans
cnt=1
ANS=deque(visit[:m])
for i in range(1,n-m+1):
    ans -= ANS.popleft()
    ans += visit[m + i - 1]
    ANS.append(visit[m + i - 1])
    if ans==MAX:
        cnt += 1
    elif ans>MAX:
        cnt = 1
        MAX=ans
if MAX==0:
    print('SAD')
else:
    print(MAX)
    print(cnt)