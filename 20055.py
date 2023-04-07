import sys
from collections import deque
n,k=map(int,sys.stdin.readline().split())
belt=list(map(int,sys.stdin.readline().split()))
belt=[belt[:n]]+[belt[n:][::-1]]
robot=[[0 for _ in range(n)]for _ in range(2)]
cnt=1
ro_loc=deque()
#####y=0 and x=n-1 일떄 로봇내림
while True:
    belt[1].append(belt[0].pop())
    belt[0].insert(0,belt[1].pop(0))
    robot[1].append(robot[0].pop())
    robot[0].insert(0, robot[1].pop(0))
    for _ in range(len(ro_loc)):
        Y,X=ro_loc.popleft()
        if Y==0 and X==n-1:
            robot[Y][X]=0
        elif Y==0 and 0<= X<n-1:
            X+=1
            ro_loc.append((Y,X))
        else:
            ro_loc.append((Y,X))
    if ro_loc:
        a=len(ro_loc)
        for _ in range(a):
            y,x=ro_loc.popleft()
            if y==0 and x==n-1:
                robot[y][x]=0
            elif y==0 and 0<=x<n-1 and belt[0][x+1]>0 and robot[0][x+1] == 0:
                if y == 0 and x+1==n-1:
                    robot[y][x]=0
                    belt[y][x+1]-=1
                else:
                    belt[0][x+1]-=1
                    robot[0][x]=0
                    robot[0][x+1]=1
                    ro_loc.append((0,x+1))
            else:
                ro_loc.append((y,x))
    if belt[0][0]>0 and robot[0][0]==0:
        belt[0][0]-=1
        robot[0][0]=1
        ro_loc.append((0,0))
    if belt[0].count(0)+belt[1].count(0) >= k:
        break
    cnt += 1
print(cnt)
