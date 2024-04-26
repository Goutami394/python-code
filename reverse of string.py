s="hey how are you"
l=list(s.split(" "))
s=""
for i in l:
   s=s+i[::-1]+" "
print(s)
