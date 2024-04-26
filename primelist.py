def isprime(x):
    for i in range(2,x//2+1):
        if x%i==0:
            return 0
    else:
        return 1
l=int(input())
u=int(input())
for i in range(l,u+1):
    a=isprime(i)
    if a==1:
        print(i)