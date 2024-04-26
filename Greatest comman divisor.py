a=int(input())
b=int(input())
m=min(a,b)
g=1
for i in range(1,m+1):
    if a%i==0 and b%i==0:
        g=i
print(g)