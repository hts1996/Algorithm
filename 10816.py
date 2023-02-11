import sys
n=int(sys.stdin.readline())
n_list=list(map(int,sys.stdin.readline().split()))
m=int(sys.stdin.readline())
m_list=list(map(int,sys.stdin.readline().split()))
def bi(a,N,key):
    low=0
    high=N-1
    while low <high:
        middle = (low + high) // 2
        if a[middle] > key:
            high = middle-1
        elif a[middle] < key:
            low = middle+1
        else:
            break
    if a[middle] == key:
        return 1
    elif a[middle]!=key:
        return 0
b = sorted(n_list)
cnt=[0]*m
a={}
for i in n_list:
    if i in a:
        a[i] += 1
    else:
        a[i] = 1
for i in range(m):
    if bi(b,n,m_list[i]) != 0:
        cnt[m_list.index(m_list[i])] = a[m_list[i]]*bi(b,n,m_list[i])
print(*cnt)