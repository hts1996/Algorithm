alp=str(input())
counting=0
sum=0
for i in range(len(alp)):
    if ord(alp[i])>=87:
        counting = 10
    elif ord(alp[i])>=84:
        counting = 9
    elif ord(alp[i])>=80:
        counting = 8
    elif ord(alp[i])>=77:
        counting = 7
    elif ord(alp[i])>=74:
        counting = 6
    elif ord(alp[i])>=71:
        counting = 5
    elif ord(alp[i])>=68:
        counting = 4
    elif ord(alp[i])>=65:
        counting = 3
    sum+=counting
print(sum)