#!/usr/bin/env python3

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Vector {self.x,self.y}"
    
    #2d vectors operations
    def add(self,tvector):
        self.x += tvector.x
        self.y += tvector.y
        return print(self.x, self.y)
    def dot(self, tvector):
        return print(self.x*tvector.x + self.y*tvector.y)
    def scale(self,scalar):
        self.x *= scalar
        self.y *= scalar
        return print(self.x,self.y) 
    
    def magnitude(self):
        return print((self.x**2 + self.y**2)**0.5)

#random vectors    
# v1 = Vector(1,2)
# v2 = Vector(3,4)
# print(v1)
# print(v2) 

# #operations
# v1.dot(v2)
# v1.magnitude()
# v1.add(v2)
# v1.scale(25)

class Matrix:
    def __init__(self,matrix,dims):
        self.matrix = matrix
        self.dims = dims

    def add(self,tmatrix):
        new_matrix = []
        for i in range(self.dims[0]):
            new_matrix.append([])
            for e in range(self.dims[1]):
                val = self.matrix[i][e] + tmatrix.matrix[i][e]
                new_matrix[i].append(val)
        return print (new_matrix)
    
    def scalar (self,scalar):
        for a in range(self.dims[0]):
            for b in range(self.dims[1]):
                self.matrix[a][b] *= scalar 
        return print(self.matrix)
    
#random matrices
m1 = Matrix([[1,2],[3,4]],(2,2))
m2 = Matrix([[5,6],[7,8]],(2,2))

#matrix operations                                                      
m1.add(m2) 
m1.scalar(25)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             






