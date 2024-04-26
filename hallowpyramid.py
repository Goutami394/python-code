n=int(input())
for i in range(1,n+1):
 if i==1 or i==n:
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(0,2*i-1):
        print("*",end="")
    print()
 else:
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(0,2*i-1):
     if j==0 or j==2*i-2:
        print("*",end="")
     else:
        print(" ",end="")
    print()
