num=int(input())

list_1=[]
for i in range(num):
    ox_list=list(str(input()))
    x=0
    score=0
    for j in range(len(ox_list)):
        if ox_list[j]=='O':
            x+=1
            score +=x
        else:
            x=0
    list_1.append(score)
for i in range(len(list_1)):
    print(list_1[i],end="\n")