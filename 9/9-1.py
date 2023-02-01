a,b=map(int,input().split())
list_a=[list(map(int,input().split())) for _ in range(a)]
list_b=[list(map(int,input().split())) for _ in range(a)]
list_c=[[0]*b for _ in range(a)]
for i in range(a):
    for j in range(b):
        list_c[i][j]=list_a[i][j]+list_b[i][j]
for k in range(a):
    print(*list_c[k])