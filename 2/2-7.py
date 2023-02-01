num1,num2,num3=map(int,input().split())
if num1==num2 and num1==num3:
    print(10000+num1*1000)
elif num1==num2 or num2==num3 or num3==num1:
    if num1==num2:
        print(num1*100+1000)
    elif num2==num3:
        print(num2*100+1000)
    elif num3==num1:
        print(1000+100*num1)
elif num1!=num2 and num2!=num3 and num3!=num1:
    if num1>num2:
        if num1>num3:
            print(num1*100)
        else:
            print(num3*100)
    else:
        if num2>num3:
            print(num2*100)
        else:
            print(num3*100)