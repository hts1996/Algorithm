# 시간초과
# num=int(input())
# def bu(a,b):
#     if a == 0:
#         return b
#     elif b==1:
#         return 1
#     else:
#         return bu(a,b-1)+bu(a-1,b) 
# for i in range(num):
#     x=int(input())
#     y=int(input())
#     print(bu(x,y))
num=int(input())
b=[]

for i in range(15):
    a=[]
    for j in range(15):
        sum=0
        if i==0:
            sum=j+1
            a.append(sum)
        elif j == 0:
            sum =1
            a.append(sum)
        elif i>0 and j >0:
            sum=b[i-1][j]+a[j-1]
            a.append(sum)
    b.append(a)
for k in range(num):
    num1=int(input())
    num2=int(input())
    print(b[num1][num2-1])

