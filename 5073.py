while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    if a==b==c:
        print('Equilateral')
        continue
    elif a==b or b==c or a==c:
        if max([a,b,c])>=(sum([a,b,c])-max([a,b,c])):
            print('Invalid')
        else:
            print('Isosceles')
        continue
    elif a!=b!=c:
        if max([a,b,c])>=(sum([a,b,c])-max([a,b,c])):
            print('Invalid')
        else:
            print('Scalene')
        continue
