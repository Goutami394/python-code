n=int(input())
s=[1,2,3,4,5]
if n>len(s):
    n=n%len(s)
print(s[-n::]+s[0:-n])