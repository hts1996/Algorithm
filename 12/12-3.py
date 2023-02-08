num=int(input())
a=[]
for i in range(num):
    b=list(map(int,input().split()))
    a.append(b)
c=[]
for j in range(num):
    cnt=0
    for k in range(num):
        if a[j][0]<a[k][0] and a[j][1]<a[k][1]:
            cnt+=1
    c.append(cnt+1)
print(*c)
##########################
# r=[0 for _ in range(num)]
# max=4
# n=1
# for x in range(num):
#     count=0
#     for l in range(num):
#         if c[l]==max:
#             r[l]=n
#     count=c.count(max)
#     n+=count
#     max-=1
# print(*r)