p=int(input())
while p:
    n=int(input())
    a=list(map(int,input().split()))
    c=0
    for i in range(1,n):
        if a[i-1]>a[i]:
            c+=1
    if c==0:
        print(c)
    else:
        print(max(a)-min(a))
    p-=1