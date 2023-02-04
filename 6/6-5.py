alp=str(input())
mod_alp=','.join(alp.upper())
set_alp=set(mod_alp.split(','))
max=0
alp_list=list(set_alp)
for i in range(len(alp_list)):
    mod_alp.count(alp_list[i])
    if mod_alp.count(alp_list[i])>max:
        max=mod_alp.count(alp_list[i])
        char=alp_list[i]
    elif mod_alp.count(alp_list[i])==max:
        char='?'
print(char)