#!/usr/bin/env python3
import numpy as np

class VectorND:
    def __init__(self,vector):
        self.vector = np.array(vector).reshape(vector.size)


    def __add__(self,ot):
        return self.vector + ot.vector
    def __sub__(self, ot):
        return self.vector - ot.vector
    def dot(self,ot):
        return np.dot(self.vector,ot.vector)
    def scale(self,scale):
        return self.vector *scale
    def magntide():
        pass
    
a = VectorND(np.arange(0,10).reshape(5,2))
b = VectorND(np.arange(5,15).reshape(5,2))


print("{} \n{} \n\n{}".format(a.vector,b.vector,a+b),
      "the dot product of {} and{} is {}".format(a.vector,b.vector,a.dot(b)),
      sep="\n")
# print(vector(a))









