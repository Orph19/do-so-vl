#!/usr/bin/env python3
import numpy as np

class Vector:
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



print(a)









