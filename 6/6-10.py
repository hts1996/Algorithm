num=int(input())
counting=num
for i in range(num):
    alp=str(input())
    num_1=len(alp)
    mod_alp=alp

    for k in range(num_1-1):
        if alp[k]==alp[k+1]:
            mod_alp=mod_alp.replace(alp[k],'',1)
        else:
            alp=alp
    num_2=0
    for l in range(len(mod_alp)):
        if len(mod_alp)<=2:
            pass
        else:
            for n in range(l+1, len(mod_alp)):
                if mod_alp[l] == mod_alp[n]:
                    num_2+=1
                else:
                    pass
    if num_2>0:
        counting-=1
    else:
        pass
print(counting)