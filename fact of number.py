def recur(x):
   print(x)
   x+=1
   recur(x)
recur(1)

#factorial of no.
#def fact(x):
#    if x==1:
#        return x
#    return x*fact(x-1)
#n=int(input())
#a=fact(n)
#print(a)


#factorial of no.
# def fact(a,x):
#     if a==x:
#         return x
#     return a*fact(a+1,x)
# n=int(input())
# a=fact(1,n)
# print(a)


# fibonacci series
# def fib(x):
#     if x<=1:
#         return x
#     return fib(x-1)+fib(x-2)
# n=int(input())
# a=fib(n)
# print(a)


#reverse number in recurssion
# def rev(x,res):
#     if x<=0:
#         return res
#     rem=x%10
#     res=res*10+rem
#     return rev(x//10,res)
# n=int(input())
# res=0
# a=rev(n,res)
# print(a)


#power of three recurssion
# def power(i,x):
#     if x==1:
#         return True

    
#     elif 3**i==x:
#         return True
        
#     elif 3**i>=x:
#         return False
    
#     else:
#         return power(i+1,x)
# n=int(input())
# a=power(1,n)
# print(a)




