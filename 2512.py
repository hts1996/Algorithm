import sys
from collections import deque
n=int(sys.stdin.readline())
tax=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
ans=0
if sum(tax) <= m:
    ans=max(tax)
else:
    tax.sort()
    tax = deque(tax)
    while True:
        if min(tax)>=m//len(tax):
            ans=m//len(tax)
            break
        else:
            a = tax.popleft()
            m-=a
            if min(tax)<=m//len(tax):
                pass
            else:
                ans=m//len(tax)
                if ans<a:
                    ans=a
                break
print(ans)