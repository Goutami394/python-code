s="goutami"
p=set(s)
for i in p:
    c=0
    for j in s:
        if i==j:
            c+=1
    print(i,"-",c)