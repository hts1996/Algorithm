num1,num2=map(int,input().split())
if num1>0 and num1<24:
    if num2>=45:
        print(f'{num1} {(num2-45)}')
    else:
        print(f'{num1-1} {60-abs(num2-45)}')
elif num1 == 0:
    if num2>=45:
        print(f'{num1} {(num2-45)}')
    else:
        print(f'{num1+23} {60-abs(num2-45)}')