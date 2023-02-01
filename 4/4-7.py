num=int(input())
score_list=list(map(int,input().split()))
max=score_list[0]
for i in range(num):
    if score_list[i]>=max:
        max=score_list[i]
mod_list=[]
for j in range(len(score_list)):
    mod_list.append(int(score_list[j])*100/int(max))
print(sum(mod_list)/len(mod_list))