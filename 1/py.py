#!/usr/bin/env python3

class Vector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Vector {self.x,self.y}"
    def add(self,tvector):
        self.x += tvector.x
        self.y += tvector.y
        return print(self.x, self.y)
    def scale(self,scalar):
        self.x *= scalar
        self.y *= scalar
        return print(self.x,self.y) 
    def dot(self, tvector):
        return print(self.x*tvector.x + self.y*tvector.y)
    
    def magnitude(self):
        return print((self.x**2 + self.y**2)**0.5)

#random vectors    
v1 = Vector(1,2)
v2 = Vector(3,4)
print(v1)
print(v2) 

#operations
v1.dot(v2)
v1.magnitude()
v1.add(v2)
v1.scale(25)


