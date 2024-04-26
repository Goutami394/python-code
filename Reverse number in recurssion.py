#reverse number in recurssion
def rev(x,res):
    if x<=0:
        return res
    rem=x%10
    res=res*10+rem
    return rev(x//10,res)
n=int(input())
res=0
a=rev(n,res)
print(a)