import sys
n,G=map(str,sys.stdin.readline().split())
v=[]
ans=0
cnt=1
Game={'Y':2,'F':3,'O':4}
people=[]
for i in range(int(n)):
    a=sys.stdin.readline().rstrip()
    people.append(a)
a=set(people)
ans = len(a)//(Game[G]-1)
print(ans)
