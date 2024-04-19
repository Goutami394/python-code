n=int(input())
r=0
i=1
for i in range(1,n):
    if n%i==0:
        r=r+i
       
if r>n:
    print("abundant number")
else:
    print("not abundant number")