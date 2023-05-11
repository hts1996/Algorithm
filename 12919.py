import sys
def dfs(word):
    global t,ans
    if word==s:
        ans=1
        return
    if len(word) <2:
        return
    if word[0]=='B':
        if word[len(word) - 1] == 'A':
            dfs(word[:len(word) - 1])
        word=word[1:]
        dfs(word[::-1])
    if word[len(word)-1]=='A':
        dfs(word[:len(word)-1])
    return
s=sys.stdin.readline().rstrip()
t=sys.stdin.readline().rstrip()
ans=0
dfs(t)
print(ans)