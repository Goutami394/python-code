n=int(input())
for i in range(2,n):
    if n%i==0:
        print("Not prime no.")
        break
else:
    print("prime no.")