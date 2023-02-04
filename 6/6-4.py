num=int(input())
def QR():
    alp=str(input())
    rlt=""
    for i in range(2,len(alp)):
        if len(alp) < 1:
            pass
        else:
            rlt += alp[i]*int(alp[0])
    return rlt
for i in range(num):
    print(QR())