import sys
n=int(sys.stdin.readline())
if n%4 ==0 or n%2==0 or n%6==0:
    print('CY')
else:
    print('SK')