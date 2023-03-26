from collections import deque
import sys
dy=[1,0,-1,0]
dx=[0,1,0,-1]
m,n=map(int,sys.stdin.readline().split())
alp=[]
for i in range(m):
    alp.append(list(map(int,input())))
v=[]
queue=deque()
for i in range(n):
    if alp[0][i] == 0:
        queue.append((0,i))
        alp[0][i] = 1
ans='NO'
while queue:
    y,x=queue.popleft()
    for k in range(4):
        yy=y+dy[k]
        xx=x+dx[k]
        if 0<=yy<m and 0<=xx<n and alp[yy][xx] ==0:
            if yy == m-1:
                ans='YES'
            alp[yy][xx]=1
            queue.append((yy,xx))
cnt=0
print(ans)