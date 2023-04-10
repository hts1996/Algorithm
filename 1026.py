import sys
n=int(sys.stdin.readline())
num1=list(map(int,sys.stdin.readline().split()))
num2=list(map(int,sys.stdin.readline().split()))
num1.sort(reverse=True)
num2.sort()
MIN=0
for i in range(n):
    MIN+=num1[i]*num2[i]
print(MIN)