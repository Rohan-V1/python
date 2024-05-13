def equal(c,d):
    print("Strings are: "+ c,d)
    e=0
    if(len(c)!=len(d)):
        return False
    else:
        for i in range(len(c)):
            if(c[i]!=d[i]):
                e+=1
        if(e>1):
            return False
        else:
            return True
        
a=input("Enter string 1: ")
b=input("Enter string 2: ")
print(equal(a,b))
