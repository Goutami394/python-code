a=[1,2,3,4,5,6,7,8,9,10]
even=a[1::2]
odd=a[-2::-2]
l=[]
l.extend(even)
l.extend(odd)
print(l)