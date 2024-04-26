
# fibonacci series
def fib(x):
    if x<=1:
        return x
    return fib(x-1)+fib(x-2)
n=int(input())
a=fib(n)
print(a)
