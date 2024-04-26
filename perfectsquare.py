n=int(input())
i=1
while i**2<n:
    i+=1
if i**2==n:
    print("perfect square")
else:
    print("not perfect square")