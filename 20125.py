import sys
n=int(sys.stdin.readline())
cookie=[]
dy=[1,0,-1,0]
dx=[0,1,0,-1]
for i in range(n):
    cookie.append(list(map(str,input())))
hearts=[]
for i in range(n):
    for j in range(n):
        if cookie[i][j] == '*':
            cnt = 0
            for k in range(4):
                y=i+dy[k]
                x=j+dx[k]
                if 0<=y<n and 0<=x<n and cookie[y][x] == '*':
                    cnt+=1
            if cnt == 4:
                hearts=(i+1,j+1)
                break
la=0
for i in range(1,n):
    y,x=hearts
    if 0<=x-1-i <n and cookie[y-1][x-1-i] == '*':
        la+=1
    else:
        break
ra=0
for i in range(1,n):
    y,x=hearts
    if 0<=x-1+i <n and cookie[y-1][x-1+i] == '*':
        ra+=1
    else:
        break
body=0
for i in range(1,n):
    y,x=hearts
    if 0<=y-1+i <n and cookie[y-1+i][x-1] == '*':
        body+=1
    else:
        tail=(y-1+i-1,x-1)
        break
ll=0
for i in range(1,n):
    y,x=tail
    if 0<=y+i<n and cookie[y+i][x-1] == '*' :
        ll+=1
    else:
        break
rl=0
for i in range(1,n):
    y,x=tail
    if 0<=y+i<n and cookie[y+i][x+1] == '*' :
        rl+=1
    else:
        break
print(*hearts)
print(la,ra,body,ll,rl)
