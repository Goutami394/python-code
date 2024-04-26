l="5678+-*"
a=[]
for i in l:
    if i.isdigit():
        a.append(int(i))
    else:
        op2=a.pop()
        op1=a.pop()
        if i=="+":
            a.append(op1+op2)
        elif i=="-":
            a.append(op2-op1)
        elif i=="*":
            a.append(op1*op2)
        elif i=="/":
            a.append(op1/op2)
print(a)