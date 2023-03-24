from collections import deque
import sys
n,m=map(int,sys.stdin.readline().split())
pic=[]
dy=[1,0,-1,0]
dx=[0,1,0,-1]
for i in range(n):
    pic.append(list(map(int,sys.stdin.readline().split())))
v=[[False for _ in range(m)] for _ in range(n)]
t_cnt=0
size=[]
for i in range(n):
    for j in range(m):
        if pic[i][j] != 1:
            continue
        elif v[i][j] == True:
            continue
        elif pic[i][j] == 1 and v[i][j] == False:
            t_cnt+=1
            queue=deque()
            queue.append((i,j))
            cnt=0
            v[i][j] = True
            while queue:
                y,x=queue.popleft()
                cnt+=1
                for k in range(4):
                    yy=y+dy[k]
                    xx=x+dx[k]
                    if yy<0 or yy>=n:
                        continue
                    elif xx<0 or xx>=m:
                        continue
                    elif pic[yy][xx]!=1:
                        continue
                    elif v[yy][xx] == False:
                        queue.append((yy, xx))
                        v[yy][xx] = True
            size.append(cnt)
if len(size)==0:
    ans=0
else:
    ans=max(size)
print(t_cnt)
print(ans)