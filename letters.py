n=int(input())
for i in range(2*n):
 if i>=0 and i<=n:
  if i==0 or i==n:
    for j in range(n):
       print("*",end=" ")
    print()
  else: 
    for j in range(n):
     if j==0:
       print("*",end=" ")
    print()
 else:
       for i in range(1,n+1):
          if 1==n:
            for j in range (1,n+1):
             print("*",end="")
            
