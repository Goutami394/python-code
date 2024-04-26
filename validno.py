n=input()
if len(n)==10:
    if n[0]=='6' or n[0]=='7' or n[0]=='8' or n[0]=='9':
        if n.isdigit():
            print("valid")
            exit
        else:
            print("not valid")
    else:
        print("invalid")
else:
    print("not valid")