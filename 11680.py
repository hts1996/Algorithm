import sys
n,m=map(int,sys.stdin.readline().split())
num_list=[list(map(int,input().split())) for _ in range(n)]
sum_list=[[0]*(n+2) for _ in range(n+2)]
for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            sum_list[i+1][j+1] = num_list[i][j]
        elif i ==0 and j>0:
            sum_list[i+1][j+1] = num_list[i][j]+sum_list[i+1][j]
        elif j == 0 and i>0:
            sum_list[i+1][j+1] = num_list[i][j]+sum_list[i][j+1]
        else:
            sum_list[i+1][j+1] = num_list[i][j]+sum_list[i+1][j]+sum_list[i][j+1]-sum_list[i][j]
for k in range(m):
    x1,y1,x2,y2 = map(int,sys.stdin.readline().split())
    x=x2-x1
    y=y2-y1
    ans=sum_list[x2][y2]-sum_list[x2-x-1][y2]-sum_list[x2][y2-y-1]+sum_list[x2-x-1][y2-y-1]
    print(ans)