num=int(input())
sum=0
for i in range(num):
    sum+=num
    num-=1
    if num == 0:
        print(sum)