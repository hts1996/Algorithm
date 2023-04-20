import sys
from collections import deque
n,m=map(int,sys.stdin.readline().split())
room=[]
dy=[1,0,-1,0,1,1,-1,-1]
dx=[0,1,0,-1,1,-1,1,-1]
for _ in range(n):
    room.append(list(map(int,sys.stdin.readline().split())))
MAX=0
Q=deque()
for i in range(n):
    for j in range(m):
        if room[i][j] == 1:
            Q.append((i,j))
while Q:
    y,x = Q.popleft()
    for k in range(8):
        yy=y+dy[k]
        xx=x+dx[k]
        if 0<=yy<n and 0<=xx<m and room[yy][xx]==0:
            Q.append((yy,xx))
            room[yy][xx] = room[y][x] + 1
            if MAX<room[yy][xx]:
                MAX=room[yy][xx]
        elif 0<=yy<n and 0<=xx<m and room[yy][xx]!=0:
            if room[yy][xx]>room[y][x]+1:
                room[yy][xx]=room[y][x]+1
                if MAX < room[yy][xx]:
                    MAX = room[yy][xx]
print(MAX-1)