num=int(input())
for i in range(num):
    num_list=list(map(int,input().split()))
    sum=0
    for j in range(1,len(num_list)):
        sum+=num_list[j]
    avg=sum/num_list[0]
    x=0
    for k in range(1,len(num_list)):
        if num_list[k]>avg:
            x+=1
        else:
            pass

    print("{:.3f}%".format(x/num_list[0]*100))
