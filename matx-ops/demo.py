#!/usr/bin/env python3
from oopmatrix import FMatrix,Vector

# #random vectors for testing    
v1 = Vector([1,3,12])
v2 = Vector([3,4,353])

# #vector operations
dot_product = "the dot product of {} and {} is {}".format(v1.vector,v2.vector,v1.dot(v2))
norm = "the norm of {} is {}".format(v1.vector,v1.magnitude())
addition = "the sum of {} and {} is {}".format(v1.vector,v2.vector,v1+v2)
subtraction = "the subtraction of {} and {} is {}".format(v1.vector,v2.vector,v1-v2)
scaling = "the scale of {} by 2 is {}".format(v1.vector,v1.scale(2))
print(dot_product,norm,addition,subtraction,scaling,sep="\n")


# random matrices
m1 = FMatrix([[1,2],[2,4],[5,6]],(3,2))
m2 = FMatrix([[5,6],[4,4],[3,4]],(3,2))
m3 = FMatrix([[4,5,6]],(1,3))
m4 = FMatrix([[0,4,32],[9,10,3],[10,1,12]],(3,3))

#matrix operations
addition = "the sum of {} and {} is \n{}".format(m1.matrix,m2.matrix,m1.add(m2))
scalar = "the scale of {} by 2 is \n{}".format(m1.matrix,m1.scale(2))
mul = "the multiplication of {} and {} is \n{}".format(m3.matrix,m4.matrix,m3.mul(m4))    

# print(addition,scalar,mul,sep="\n")
