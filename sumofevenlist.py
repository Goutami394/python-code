s=[1,2,3,4,5,6,7,8]
even=0
odd=0
for i in s:
    if i%2==0:
        even=even+i
    else:
        odd=odd+i
print("even=",even) 
print("odd=",odd)   