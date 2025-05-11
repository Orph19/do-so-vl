#!/usr/bin/env python3
import numpy as  np
import pandas as pd
import csv
import pathlib 

sep = lambda a='------------' :print(a) #print "---" lines to separate content
p = lambda i: print(i,end='\n-------------\n') #short for print(),added the lines to avoid using sep()
def gen(r:int,c:int,s=0,e=100): #generates a random set of number and puts them into a csv file
    generator = np.random.randint(s,e,r*c).reshape(r,c)*0.75
    generator+=np.random.randint(-e,s,r*c).reshape(r,c)*0.24
    dt = pd.DataFrame(generator,index=[f'row{i}'for i in range(generator.shape[0]) ])
    dt.columns = [f'col{i}'for i in range(generator.shape[1])]
    dt.to_csv('dts.csv')

#DATA FRAME

a = pd.DataFrame({'Yes': [3,32,123,2],
                  'NO':[23,32,23,3],
                  "Maybe":[1.,2,2,3]},
                  index=['A','B','C','D'])
# print(a)

#SERIES
b = pd.Series([1,341,32,13,1],
              index = ['a','b','c','d','e'],
              name= 'Test')
# print(b)

#HUMBLE CSV
file = pathlib.Path('dts.csv')
with file.open('r') as f:
    reader = csv.reader(f,delimiter=",")
    for row in reader:
        pass
        # print(row)

    ##read the thing 
data = pd.read_csv('dts.csv')
# print(data.shape,'\n')
table = data.head()
# print(table,end='\n\n')

#INDEXING
atribute = a.Yes
# print(atribute)

dicti = a['NO']
# print(dicti)

# print(data['TYPE A'][0],end='\n\n')

    ##more indexing
# .iloc
diloc = a.iloc[0]
diloc1 = a.iloc[:,0]
# print(diloc,end='\n\n')
# print(diloc1)
# sep()
# print(a.iloc[:2,1:])
# sep()
# print(a.iloc[-1:,:])
# sep()
# .loc, it uses the name of the colum and includes the ten in 0:10
# print(a.loc[:,'Maybe'])

#use a colum as new index
new_index= a.set_index('Maybe')
# print(new_index)


#CONDITIONALS to sort data
boollean = a.Yes == 2
p(boollean)
# print(boollean.sum())
    ##Two conditionals
boloc = a.loc[(a['NO']== 23)&(a.Maybe ==1)]
# print(boloc)

    ##Asking to see data if is in
isornot = a.loc[a.Yes.isin([1,2])]
# print(isornot)
    ##.notnull()

#ASSIGNING DATA
a['Yes'] = 1
a['NO'] = 0
a['Maybe'] = np.linspace(0,1,len(a))
# print(a)

#SUMMARY FUNCTION
# gen(23,31,0,175)
t = pd.read_csv('dts.csv')#Pandas DataFrame
sry = t.col1.unique() #show a Serie of the colum, just of the unique values 
dn = t.col0.value_counts()
# p(dn.idxmax())


##lambda
a = lambda x: 'number' if type(x)==int else 'no number' #conditionals
# p(a(1))
b = [lambda i=y:f'lambda {i}' for y in range(1,6)]#list comprehension of functions as elements
# for i in b:
#     p(i())#each function in the list needs to be called
#------------------------
#MAP()
meant = t.col23.mean()
# p(meant)
# p(t.col23)

using_map = t.col23.map(lambda i: i - meant)#for each row, new value, returns just the column
# p(using_map)
#APPLY()
def func(row):
    if row.col0 == 25:
        return 1
    
using_apply = t.apply(func, axis = 'columns')## it can modify rows and return all the Data frame, or return a new series for each index
p(t)
p(using_apply)
#BUILT IN OPERATIONS
meancol23 = t.col23.mean()
new_col23 = t.col23 - meancol23
# p(new_col23)
# p(type(t.col1.idxmax()))
# -----------------------
a = 'v spaecif da ada dada'
p('specif' in a )
