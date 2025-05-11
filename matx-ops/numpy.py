#!/usr/bin/env python3
import numpy as np
import pandas as pd
import pathlib
import csv
from numpy.random import default_rng
np.random.seed(0)

pt = lambda a,b: print(a,b,sep='\n',end='\n-------------\n')
p = lambda a: print(a, end='\n-------------\n')
#--------------------

a = np.array([a for a in range(-10,40)]).reshape(5,10)##Array and reshape
# pt(a,a.shape)
swap = np.swapaxes(a,0,1)#Swap specified axes
# pt(swap,swap.shape)
# ------------------------
#MAX()
# p(a.max(axis=1))#counting the axis from left to right, in (1,3,6), the 0 axis is 1
# -----------------------------

#BROADCASTING, and np.arange()
ar = np.arange(45).reshape(3,5,3) 
br = np.arange(35).reshape(1,7,5)
# p(ar+br) #can't broadcast

na = ar.reshape(9,1,5) #works if it have '1' as the value of the diferent axis
nb = br.reshape(1,7,5)
# p(na+nb) #array of (9,7,5)
#----------------------------------
#INDEXING
square = np.array([
    [16, 3, 2, 13],
    [5, 10, 11, 8],
    [9, 6, 7, 12],
    [4, 15, 14, 1]
])

for i in range(4):
    assert square[:,i].sum() == 34
    assert square[i,:].sum() == 34
# ---------------------------
#MASKING AND FILTERING
#MASK
num = np.linspace(-45,56,45,dtype=int).reshape(9,-1)
mask = num % 4 == 0
# p(num[mask]) #just show the ones who are true
#same logic:
# p(num[num%4==0])

rng = default_rng()
val = rng.standard_normal(10000)

filter_val = val[(val > -2*val.std())&(val < 2* val.std())]#values betwen 
# pt(filter_val.size,val.size)
# p(filter_val.size/val.size) #95% of the values are 2std away of the mean
# ------------------------
#TRANSPOSING, SORTING, CONCATENATING
    #transpose 
sample= np.random.randint(-11,15,28).reshape(4,-1)
another = np.random.randint(-13,45,28).reshape(4,-1)
# pt(sample,sample.T)s
p(sample)
p(another)
    #sort
# p(np.sort(sample))
# p(np.sort(sample,axis=None))
# p(np.sort(sample,axis=0))
    #concatening
# p(np.concatenate((sample,another)))
# p(np.vstack((sample,another)))
# p(np.hstack((sample,another)))

#STRUCTURED ARRAY
structured = np.array([('A',56),('B',57)],dtype=[('Name',str,10),('Assi',int)])
p(structured['Name'])
