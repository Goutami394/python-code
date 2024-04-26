n=int(input())
i=1
while 2**i<n:
    i+=1
if 2**i==n:
    print("power of two")
else:
    print("not power of two")