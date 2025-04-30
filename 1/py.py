#!/usr/bin/env python3

class Vector:
    def __init__(self,vector,dimension):
        self.vector = vector
        self.dimension = dimension
    def __str__(self):
        return f"Vector {self.vector} of dimension {self.dimension}"
    
    #nd vectors operations
    def add(self,tvector):
        new_vector = []
        for i in range (self.dimension): 
            val = self.vector[i] + tvector.vector[i]
            new_vector.append(val) 
        return new_vector
    
    def dot(self, tvector):
        dot_vector = 0
        for i in range (self.dimension): 
            val = self.vector[i] * tvector.vector[i]
            dot_vector += val
        return dot_vector
    
    def scale(self,scalar):
        scaled_vector = []
        for i in range (self.dimension): 
            val = self.vector[i] * scalar
            scaled_vector.append(val)
        return scaled_vector
    
    def magnitude(self):
        norm_vector = 0
        for i in range (self.dimension):
            val = self.vector[i]** 2
            norm_vector += val   
        return norm_vector**0.5

# random vectors    
# v1 = Vector([1,2,4],3)
# v2 = Vector([3,4,353],3)
# print(v1)
# print(v2) 

# #operations
# dot_product = "the dot product of {} and{} is {}".format(v1.vector,v2.vector,v1.dot(v2))
# norm = "the norm of {} is {}".format(v1.vector,v1.magnitude())
# addition = "the sum of {} and {} is {}".format(v1.vector,v2.vector,v1.add(v2))
# scaling = "the scale of {} by 2 is {}".format(v1.vector,v1.scale(2))

# print(dot_product,norm,addition,scaling,sep="\n")

class Matrix:
    def __init__(self,matrix,dims):
        self.matrix = matrix
        self.dims = dims

    def add(self,tmatrix):
        sum_matrix = []
        for i in range(self.dims[0]):
            sum_matrix.append([])
            for e in range(self.dims[1]):
                val = self.matrix[i][e] + tmatrix.matrix[i][e]
                sum_matrix[i].append(val)
        return sum_matrix
    
    def scalar (self,scalar):
        scaled_matrix = []
        for a in range(self.dims[0]):
            scaled_matrix.append([])
            for b in range(self.dims[1]):
                val = self.matrix[a][b] * scalar 
                scaled_matrix[a].append(val)
        return scaled_matrix
    
    #to transpose tmatrix
    def transpose(self):
        trsp_matrix = []
        for w in range(self.dims[1]):
            trsp_matrix.append([])
            for q in range(self.dims[0]):
               trsp_matrix[w].append(self.matrix[q][w])
        return trsp_matrix

    def mul(self,tmatrix):
        mul_matrix = []
        for i in range(self.dims[0]):
            mul_matrix.append([])
            for e in range(tmatrix.dims[1]):
                v1 = Vector(self.matrix[i],self.dims[1])
                v2 = Vector(tmatrix.transpose()[e],tmatrix.dims[0])
                val = v1.dot(v2)
                mul_matrix[i].append(val)
        return mul_matrix
          
# random matrices
m1 = Matrix([[1,2],[2,4],[5,6]],(3,2))
m2 = Matrix([[5,6],[4,4],[3,4]],(3,2))
m3 = Matrix([[4,5,6]],(1,3))
m4 = Matrix([[0,4,32],[9,10,3],[10,1,12]],(3,3))

addition = "the sum of {} and {} is {}".format(m1.matrix,m2.matrix,m1.add(m2))
scalar = "the scale of {} by 2 is {}".format(m1.matrix,m1.scalar(2))
mul = "the multiplication of {} and {} is {}".format(m3.matrix,m4.matrix,m3.mul(m4))    

print(addition,scalar,mul,sep="\n")






