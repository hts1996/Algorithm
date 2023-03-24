n,m=map(int,input().split())
num=list(range(1,n+1))
for i in range(m):
    a,b,c=map(int,input().split())
    dum=num[a-1:b]
    dum=num[c-1:b]+num[a-1:c-1]
    num=num[:a-1]+dum+num[b:]
print(*num)