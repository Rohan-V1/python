num=int(input("Enter the number of elements "))
a=[]
for i  in range(num):
    n=int(input("Enter the number {} ".format(i+1)))
    a.append(n)
print("Original List ",a)
s=set(a)
unique_list=list(s)
print("unique elements= ",unique_list)
single_list=[]
for i in a:
    if a.count(i)==1:
        single_list.append(i)
print("the elements are: ",single_list)
