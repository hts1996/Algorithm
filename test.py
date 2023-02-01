import sys
input = sys.stdin.readline
n,m=map(int,input().split())
list_num=list(map(int,input().split()))
sum=0
total_sum=[0]
for i in list_num:
    sum+=i
    total_sum.append(sum)
print(total_sum)
for j in range(m):
    a,b=map(int,input().split())
    hap=total_sum[b]-total_sum[a-1]
    print(hap)