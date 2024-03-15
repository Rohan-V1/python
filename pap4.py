t1=(1,2,5,7,9,2,4,6,8,10)
print("the first half of the tuple: ",t1[:5])
print("the second half of the tuple: ",t1[5:])
li=[]
for i in range(len(t1)):
    if t1[i]%2==0:
        li.append(t1[i])
t_even=tuple[li]
print("New tuple with even element from t1: ",t_even)
t2=(11,13,15)        
print("The first tuple: ",t1)
print("The second tuple: ",t2)
res=t1+t2
print("the tuple after concantenation: ",res)
print("the maximum value in concantenated tuple: ",max(res))
print("the minimun value in concantenated tuple: ",min(res))