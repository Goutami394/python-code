n=int(input())
for i in range(1,n+1):
    for j in range(1,n-i+1):
        print(" ",end="")
    for j in range(0,2*i-1):
        print("*",end="")
    for j in range(1,(n-i+1)*2):
     if j!=(n-i+1)*2-1:
        print(" ",end="")
    for j in range(0,2*i-1):
        print("*",end="")
    print()
for i in range((2*n-1),0,-1):
    for j in range(1,(2*n)-i):
        print(" ",end="")
    for j in range(0,2*i-1):
        print("*",end="")
    print()