n=int(input())
stars=[]
ori_star=[' ' for _ in range(2*n-1)]
a=[]
for i in range(n):
    star=ori_star[::]
    star[n-1-i] = '*'
    star[n-1+i]='*'
    ori_star = star
    star=''.join(star)
    star=star.rstrip(' ')
    stars.append(star)

demo=stars[::]
demo.pop()
stars=stars+demo[::-1]
for j in range(2*n-1):
    print(stars[j])