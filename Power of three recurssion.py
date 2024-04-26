#power of three recurssion
def power(i,x):
    if x==1:
        return True

    
    elif 3**i==x:
        return True
        
    elif 3**i>=x:
        return False
    
    else:
        return power(i+1,x)
n=int(input())
a=power(1,n)
print(a)

