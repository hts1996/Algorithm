import sys
n=int(sys.stdin.readline())
def preorder(s):
    global ans1
    if s == '.':
        return
    else:
        ans1+=s
        preorder(tree[s][0])
        preorder(tree[s][1])
def midorder(s):
    global ans2
    if s == '.':
        return
    else:
        midorder(tree[s][0])
        ans2+=s
        midorder(tree[s][1])

def postorder(s):
    global ans3
    if s == '.':
        return
    else:
        postorder(tree[s][0])
        postorder(tree[s][1])
        ans3+=s
tree={}
for _ in range(n):
    node,l,r=map(str,sys.stdin.readline().split())
    tree[node]=[l,r]
ans1=''
ans2=''
ans3=''
preorder('A')
midorder('A')
postorder('A')
print(ans1)
print(ans2)
print(ans3)
