num1=int(input())
num2=int(input())
if num1 > 0 :
    if num2 > 0 :
        print(1)
    elif num2 < 0 :
        print(4)
elif num1 < 0 :
    if num2 > 0 :
        print(2)
    elif num2 < 0 :
        print(3)