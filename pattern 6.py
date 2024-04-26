n=int(input())
for i in range(1,n+1):
    for j in range(i,i+i):
        print(j*2-1,end=" ")
    print()