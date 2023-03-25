from collections import deque
import sys
dy=[1,0,-1,0]
dx=[0,1,0,-1]
n,m,k=map(int,sys.stdin.readline().split())
road=[[''for _ in range(m)]for _ in range(n)]
v=[[False for _ in range(m)]for _ in range(n)]
for i in range(k):
    a,b=map(int,sys.stdin.readline().split())
    road[a-1][b-1] = '#'
ans=[]
for i in range(n):
    for j in range(m):
        if road[i][j] == '#' and v[i][j] == False:
            queue=deque()
            queue.append((i,j))
            road[i][j] = True
            cnt=0
            while queue:
                cnt+=1
                y,x=queue.popleft()
                for o in range(4):
                    yy=y+dy[o]
                    xx=x+dx[o]
                    if 0<=yy<n and 0<=xx<m and road[yy][xx] == '#' and v[yy][xx] == False:
                        queue.append((yy,xx))
                        v[yy][xx] = True
            ans.append(cnt)
print(max(ans))