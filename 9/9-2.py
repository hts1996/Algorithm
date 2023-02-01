list_num=[list(map(int,input().split())) for _ in range(9)]
max=0
for i in range(9):
    for j in range(9):
        if list_num[i][j] > max:
            num=[]
            max=list_num[i][j]
            num.append([i+1,j+1])
        elif list_num[i][j] == max and max > 0:
            max=max
            num.append([i+1,j+1])
        elif list_num[i][j] == 0 and max == 0:
            num_1=[]
            max = 0
            num_1.append([i+1,j+1])

if max == 0:
    print(max)
    print(*num_1[0])
else:
    print(max)
    print(*num[0])