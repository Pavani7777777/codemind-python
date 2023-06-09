n=int(input())
temp=n
r=0
while n:
    d=0
    d=n%10
    r=r*10+d
    n//=10
if (temp==r):
    print(True)
else:
    print(False)
    