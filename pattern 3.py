n=int(input())
for i in range(0,n):
    for j in range(i,n+i):
        print(chr(65+j),end=" ")
    print()