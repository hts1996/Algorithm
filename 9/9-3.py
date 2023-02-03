T=int(input())
cnt=[[[0] for _ in range(101)] for _ in range(101)]
for t in range(T):
    a,b=map(int,input().split())
    for i in range(10):
        for j in range(10):
            cnt[101-b-i][a+j]=1
sum=0
for k in range(len(cnt)):
    sum+=cnt[k].count(1)
print(sum)