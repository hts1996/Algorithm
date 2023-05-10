import sys
from collections import deque
n,k=map(int,sys.stdin.readline().split())
cnt=0
CNT=[10000000 for _ in range(100001)]
CNT[n]=1
loc=deque()
loc.append((k,cnt))
ans=0
MIN=100000000
while loc:
    a,b=loc.popleft()
    if a == n:
        ans = b
        break
    if a%2==1:
        pass
    else:
        if a/2==n:
            ans=b
            break
        else:
            if 0 <= a / 2 < 100001:
                if CNT[int(a/2)]==1:
                    pass
                else:
                    loc.append((int(a/2),b))
                    CNT[int(a/2)] = 1
    if a+1==n:
        ans=b+1
        break
    else:
        if 0 <= a + 1 < 100001:
            if CNT[a+1] == 1:
                pass
            else:
                loc.append((a+1,b+1))
                CNT[a + 1] = 1
    if a-1==n:
        ans=b+1
        break
    else:
        if 0 <= a - 1 < 100001:
            if CNT[a-1]==1:
                pass
            else:
                loc.append((a-1,b+1))
                CNT[a-1]=1
print(ans)