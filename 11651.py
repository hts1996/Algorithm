def msort(arr):
    if len(arr) == 1:
        return arr
    m=(len(arr))//2
    left=arr[:m]
    right=arr[m:]
    left=msort(left)
    right=msort(right)
    return merge(left,right)
def merge(l,r):
    ans=[]
    s1=s2=0
    while True:
        if s1 == len(l) and s2 == len(r):
            break
        if s1 != len(l) and s2 != len(r):
            if l[s1][1]<r[s2][1]:
                ans.append(l[s1])
                s1+=1
            else:
                if l[s1][1]==r[s2][1]:
                    if l[s1][0]<r[s2][0]:
                        ans.append(l[s1])
                        s1+=1
                    else:
                        ans.append(r[s2])
                        s2+=1
                else:
                    ans.append(r[s2])
                    s2+=1
        elif s1==len(l):
            ans.append(r[s2])
            s2+=1
        elif s2 == len(r):
            ans.append(l[s1])
            s1+=1
    return ans
import sys
n=int(sys.stdin.readline())
a=[]
for _ in range(n):
    a.append(list(map(int,sys.stdin.readline().split())))
ans=msort(a)
for i in range(n):
    print(*ans[i])