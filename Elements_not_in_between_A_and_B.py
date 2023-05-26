n=int(input())
l=list(map(int,input().split()))
k=[]
a,b=map(int,input().split())
for i in l:
    if i<a or i>b:
        k.append(i)
if len(k)==0:
    print("-1")
else:
    print(*k)