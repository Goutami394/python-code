n=int(input())
for i in range(n):
    if i==0 or i==1 or i==n-1 or i==n-2:
        for j in range(n):
            print("*",end=" ")
        print()
    else:
        for j in range(n):
            if j==0 or j==1 or j==n-1 or j==n-2:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
