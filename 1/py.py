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
v1 = Vector([1,2,4],3)
v2 = Vector([3,4,353],3)
print(v1)
print(v2) 

#operations
dot_product = "the dot product of {} and{} is {}".format(v1.vector,v2.vector,v1.dot(v2))
norm = "the norm of {} is {}".format(v1.vector,v1.magnitude())
addition = "the sum of {} and {} is {}".format(v1.vector,v2.vector,v1.add(v2))
scaling = "the scale of {} by 2 is {}".format(v1.vector,v1.scale(2))

print(dot_product,norm,addition,scaling,sep="\n")

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
        return print (sum_matrix)
    
    def scalar (self,scalar):
        for a in range(self.dims[0]):
            for b in range(self.dims[1]):
                self.matrix[a][b] *= scalar 
        return print(self.matrix)
    
    #transpose matrix
    def transpose(self):
        trsp_matrix = []
        for w in range(self.dims[1]):
            trsp_matrix.append([])
            for q in range(self.dims[0]):
               trsp_matrix[w].append(self.matrix[q][w])
        return trsp_matrix

    
    def mul(self,tmatrix):
        mul_matrix = []
        def dot_product(vector0, vector1):
            dot_scalar = 0
            for i in range (self.dims[0]): 
                vector0[i] *= vector1[i]
                dot_scalar += vector0[i]
            return dot_scalar
    
        for i in range(self.dims[0]):
            mul_matrix.append([])
            for e in range(tmatrix.dims[1]):
                val = dot_product(self.matrix[i],tmatrix.transpose()[i])
                mul_matrix[i].append(val)
        return print(mul_matrix)
          
# # random matrices
# m1 = Matrix([[1,2,5]],(1,3))
# m2 = Matrix([[5,6],[4,4],[3,4]],(3,2))

# m1.mul(m2)
# #matrix operations                                                      
# m1.add(m2) 
# m1.scalar(25)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             






