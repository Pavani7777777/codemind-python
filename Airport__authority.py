n=int(input())
l=[]
for i in range(n):
    a=int(input())
    l.append(a)
m=int(input())
c=0

for i in l:
    if i>m:
        c+=2
    else:
        c+=1
print(c)
    