#binary search
l=[9,7,78,10,5,1,0]
l.sort()
print(l)
i=0
j=len(l)-1
s=10
while i<j:
    mid=(i+j)//2
    if l[mid]==s:
        print(mid,"found")
        break
    elif l[mid]>s:
        j=mid-1
    else:
        i=mid+1
else:
    print("not found")