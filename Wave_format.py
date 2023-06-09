n=int(input())
arr=list(map(int,input().split()))
arr=sorted(arr)
l=[]
for i in range(n-1,0,-2):
    l.append(arr[i-1])
    l.append(arr[i])
    if len(l)==n:
        break
if len(arr)%2!=0:
    l.append(arr[0])
for i in l:
    print(i,end=" ")