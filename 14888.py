n=int(input())
num=list(map(int,input().split()))
cal=list(map(int,input().split()))
w=['+','-','*','/']
word=[]
for i in range(4):
    for j in range(cal[i]):
        word.append(w[i])
v=[0]*(n-1)
ans=[]
SUM=0
stack=[]
stack1=[]
ANS=[]
def dfs(s):
    global v,ans
    ans.append(num[s])
    if s == n-1:
        calcultator(ans)
        return
    for i in range(len(word)):
        if v[i] == 0:
           v[i] = 1
           ans.append(word[i])
           dfs(s+1)
           v[i] = 0
           ans.pop()
           ans.pop()
def calcultator(ans):
    global SUM
    while True:
        if len(ans)==1:
            break
        for j in range(len(ans)):
            if ans[j] == '*':
                ans=ans[:j-1]+[ans[j-1]*ans[j+1]]+ans[j+2:]
                break
            elif ans[j] == '/':
                if ans[j - 1]<0:
                    ans = ans[:j - 1] +[-(abs(ans[j - 1])//ans[j + 1])]+ ans[j + 2:]
                    break
                ans = ans[:j - 1] + [ans[j - 1] // ans[j + 1]] + ans[j + 2:]
                break
            elif ans[j] == '+':
                ans=ans[:j-1]+[ans[j-1]+ans[j+1]]+ans[j+2:]
                break
            elif ans[j] == '-':
                ans=ans[:j-1]+[ans[j-1]-ans[j+1]]+ans[j+2:]
                break
    SUM=ans[-1]

    ANS.append(SUM)
dfs(0)
print(max(ANS))
print(min(ANS))