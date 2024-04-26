#factorial of no.
def fact(x):
   if x==1:
       return x
   return x*fact(x-1)
n=int(input())
a=fact(n)
print(a)











