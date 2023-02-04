n,k=map(int,input().split())
list_score=list(map(int,input().split()))
mod_list=sorted(list_score,reverse=True)
print(mod_list[k-1])
