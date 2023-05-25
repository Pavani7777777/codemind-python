n=int(input())
n1=n**2
s=str(n)
r=int(s[::-1])
r1=r**2
s1=str(r1)
r2=int(s1[::-1])
if n1==r2:
    print("True")
else:
    print("False")