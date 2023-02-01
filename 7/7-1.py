a,b,c=map(int,input().split())
# x=1
# while True:
#     x_1=x // 10
#     x_2=x % 10
#     total = x_1*(a+b*10)+x_2*(a+b)
#     income = c*x
#     x+=1
#     if income >= total:
#         print(x)
#         break

if b>=c:
    print(-1)
else:
    print(a//(c-b)+1)