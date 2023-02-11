n=int(input())
n_list=list(map(int,input().split()))
m=int(input())
m_list=list(map(int,input().split()))
def bi(a,N,key):
    low=0
    high=N-1
    while low <=high:
        middle = (low + high) // 2
        if a[middle] > key:
            high = middle-1
        elif a[middle] < key:
            low = middle+1
        else:
            break
    if a[middle] == key:
        print(1)
    elif a[middle]!=key:
        print(0)
n_list.sort()
for i in range(m):
    bi(n_list,n,m_list[i])