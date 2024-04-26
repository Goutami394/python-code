n=int(input())
i=1
while 3**i<n:
    i+=1
if 3**i==n:
    print("power of three")
else:
    print("not power of three")