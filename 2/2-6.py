num1,num2=map(int,input().split())
num3=int(input())
if num1 > 0 and num1 < 24:
    if num1+(num2+num3)//60 >=24:
        print(f'{num1+((num2+num3)//60)-24} {((num2+num3)%60)}')
    else:
        print(f'{num1+((num2+num3)//60)} {((num2+num3)%60)}')
else:
    print(f'{num1+((num2+num3)//60)} {((num2+num3)%60)}')