import pandas as pd
data1={
    'RollNo':[101,102,103],
    'Name':['JOhn','Emma','Michel'],
    'TotalMarks':[85,92,78]
 }
df1=pd.DataFrame(data1,index=[1,2,3])
data2={
    'RollNo':[104,105,106],
    'Name':['Sophia','Oliver','Ava'],
    'TotalMarks':[98,88,95]
 }
df2=pd.DataFrame(data2,index=[4,5,6])
df_combined=pd.concat([df1,df2],axis=0)
print(df_combined)
