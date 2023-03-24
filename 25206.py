score={'A+':4.5,'A0':4.0,'B+':3.5,'B0':3.0,'C+':2.5,'C0':2.0,'D+':1.5,'D0':1.0,'F':0,'P':'pass'}
cnt=0
sum=0
for i in range(20):
    subject=list(map(str,input().split()))
    if score[subject[2]]!='pass':
        cnt+=float(subject[1])
        sum+=score[subject[2]]*float(subject[1])
print(round(sum/cnt,6))