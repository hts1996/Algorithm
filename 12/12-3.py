num=int(input())
a=[]
for i in range(num):
    b=list(map(int,input().split()))
    a.append(b)
c=[]
for j in range(num):
    cnt=0
    for k in range(num):
        if a[j][0]<a[k][0] and a[j][1]<a[k][1]:
            cnt+=1
    c.append(cnt+1)
print(*c)