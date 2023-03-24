word=[[0 for _ in range(15)] for _ in range(5)]
for i in range(5):
    wrd=input()
    for j in range(len(wrd)):
        word[i][j] = wrd[j]
for i in range(15):
    for j in range(5):
        if word[j][i]!=0:
            print(word[j][i],end='')