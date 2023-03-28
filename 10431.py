import sys
T=int(sys.stdin.readline())
for t in range(T):
    kid=list(map(int,sys.stdin.readline().split()))
    a=[]
    cnt=0
    for i in range(20):
        a.append(kid[i+1])
        if len(a)>1:
            for j in range(1,len(a)):
                if a[-j]<a[-j-1]:
                    a[-j],a[-j-1]=a[-j-1],a[-j]
                    cnt+=1
    print(kid[0],cnt)