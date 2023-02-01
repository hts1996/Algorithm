num=int(input())
sum=0
for i in range(1, num+1):
    if num == 1:
        print('1/1')
    else:
        sum+=i
        if sum>=num:
            j=abs(num-sum_1)-1
            if i % 2 == 0:
                print(f'{1+j}/{i-j}')
                break
            else:
                print(f'{i-j}/{1+j}')
                break
        sum_1=sum



