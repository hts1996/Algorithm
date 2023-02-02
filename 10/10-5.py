import sys
num=int(input())
cnt=[0]*10001
for i in range(num):
    cnt[int(sys.stdin.readline())]+=1
for k in range(10001):
    while cnt[k]>0:      
        print(k)
        cnt[k]-=1