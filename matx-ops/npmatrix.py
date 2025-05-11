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


class Matrix:
    def __init__(self,matrix):
        self.matrix = np.array(matrix)

    def __add__(self,target):
        target= np.array(target)
        try:
            new_added = self.matrix + target
        except ValueError as ve:
            print(ve)
            while True:
                new_shape:str = input('do you desire to change the shape?, enter yes or no ')
                if new_shape == 'yes' or new_shape == 'no':
                    shape_a = self.matrix.shape() 
                    shape_b = target.shape()
                    # if len(shape_a)==

        else:
            return new_added
        
    









