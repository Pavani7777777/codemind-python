a,b,c=map(float,input().split())
p=(a+b+c)/2
area=(p*(p-a)*(p-b)*(p-c))**0.5
print("%.2f"%area)