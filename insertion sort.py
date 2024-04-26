#insertion sort
b=[3,4,5,6,19,21,10]
for i in range(1,len(b)):
    j=i-1
    a=b[i]
    while j>=0 and b[j]>a:
        b[j+1]=b[j]
        j-=1
    b[j+1]=a
print(b)