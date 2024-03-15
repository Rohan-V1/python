def freq():
    str=input("enter the string: ")
    f={}
    print("the given string: \n",str)
    for i in str:
        if i in f:
            f[i]+=1
        else:
            f[i]=1
    print("The frequncy of each letter is : \n",f)

freq()            