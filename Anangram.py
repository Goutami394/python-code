
a=input()
b=input()
s=set(a)
s2=set(b)
if s==s2:
    for i in s:
        if a.count(i)!=b.count(i):
            print("not anagram")
            break
    else:
        print("anagram")
else:
    print("not anagram")