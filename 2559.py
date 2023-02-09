n,k = map(int,input().split())
a=list(map(int,input().split()))
start=0
end=0
b=[]
sum = a[start]
while True :
    if end-start < k-1:
        end+=1
        if end == n:
            pass
        else:
            sum += a[end]
    elif end-start == k-1:
        b.append(sum)
        sum-=a[start]
        start+=1
    if end == n:
        break
print(max(b))