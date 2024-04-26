l=[5,8,9,10,3,13,19]
m=l[0]
for i in range(len(l)):
    if l[i]>m:
        m=l[i]
print(m)