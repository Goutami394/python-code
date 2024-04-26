n=int(input())
a=0
t=n
d=len(str(n))
while t>0:
    rem=t%10
    a=a+(rem**d)
    t=t//10
if a==n:
    print("armstrong")
else:
    print("not armstrong")