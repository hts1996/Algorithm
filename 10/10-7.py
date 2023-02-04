list_num=list(map(int,input()))
cnt=[0]*(max(list_num)+1)
a=[0]*(len(list_num))
for i in list_num:
    cnt[i]+=1
for j in range(1,len(cnt)):
    cnt[j] = cnt[j-1]+cnt[j]
for k in list_num:
    a[-(cnt[k])]=k
    cnt[k]-=1
for l in range(len(a)):
    print(a[l],end='')