r,c=map(int,input().split())
m=[]
for i in range(r):
    l=list(map(int,input().split()))
    m.append(l)
s=0
for i in range(c):
    for j in range(r):
        if i==j or j==c-i-1:
            s=s+m[i][j]
print(s)
        