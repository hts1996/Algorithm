num=int(input())
counting=0
origin_num=num
while True:
    a=origin_num//10
    b=origin_num%10
    c=(a+b)%10
    origin_num=b*10+c
    counting+=1
    if origin_num == num:
        print(counting)
        break