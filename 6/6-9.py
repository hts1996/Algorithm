alp=str(input())
cz_alp=['c=','c-','dz=','d-','lj','nj','s=','z=']
counting=0
for i in cz_alp:
    while alp.find(i)>=0:
        if alp.find(i) >= 0:
            alp=alp.replace(i,' ',1)
            counting+=1
        else:
            pass
print(counting+len(alp.replace(' ','')))