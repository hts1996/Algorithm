num=input()
counting=0
orgin_num=num
while 1:
    if len(num)==1:
        num="0"+num
    num3=num[0]+num[1]
    num=num[-1]+num3[-1]
    counting+=1
    if num == orgin_num:
        print(counting)
        break
