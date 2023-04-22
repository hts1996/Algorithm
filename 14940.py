import sys
from collections import deque
from pprint import pprint
n,m=map(int,sys.stdin.readline().split())
road=[]
ans=[[0 for _ in range(m)]for _ in range(n)]
dy=[1,0,-1,0]
dx=[0,1,0,-1]
Q=deque()
for i in range(n):
    road.append(list(map(str,sys.stdin.readline().split())))
    for j in range(m):
        if road[i][j] == '2':
            Q.append((i,j))
            road[i][j]=0
while Q:
    y,x=Q.popleft()
    for k in range(4):
        yy=y+dy[k]
        xx=x+dx[k]
        if 0<=yy<n and 0<=xx<m and road[yy][xx] =='1':
            ans[yy][xx] = ans[y][x] + 1
            road[yy][xx]=road[y][x]+91
            Q.append((yy,xx))

for i in range(n):
    for j in range(m):
        if road[i][j] == '1':
            ans[i][j]=-1
for i in range(n):
    print(*ans[i])