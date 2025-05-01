#!/usr/bin/env python3

class Vector:
    def __init__(self,vector):
        self.vector = vector
    def __str__(self):
        return f"Vector {self.vector} of dimension {len(self.vector)}"

#n dimensional vectors operations
    def __add__(self,tvector):
        new_vector = []
        try:
            if len(self.vector) != len(tvector.vector):
                raise Exception("Add:Vectors dont match dimensions")
        except Exception as e:
            print(e,"Try changing vectors",sep="\n")
            return None  
        else:
            for i in range (len(self.vector)): 
                val = self.vector[i] + tvector.vector[i]
                new_vector.append(val)
            return new_vector
    def __sub__(self,tvector):
        new_vector = []
        try:
            if len(self.vector)!=len(tvector.vector):
                raise Exception("Sub:Vectors dont match dimensions")
        except Exception as e:
            print(e,"Try changing vectors",sep="\n")
            return None
        else:
            for i in range (len(self.vector)):
                val = self.vector[i] - tvector.vector[i]
                new_vector.append(val)
            return new_vector 
    
    def dot(self, tvector):
        dot_vector = 0
        try:
            if len(self.vector) != len(tvector.vector):
                raise Exception("dot:Vectors dont match dimensions")
        except Exception as e:
            print(e,"Try changing vectors",sep="\n")
            return None
        else:
                for i in range (len(self.vector)): 
                    val = self.vector[i] * tvector.vector[i]
                    dot_vector += val
                return dot_vector
        
    def scale(self,scalar):
        scaled_vector = []
        for i in range (len(self.vector)): 
            val = self.vector[i] * scalar
            scaled_vector.append(val)
        return scaled_vector
    
    def magnitude(self):
        norm_vector = 0
        for i in range (len(self.vector)):
            val = self.vector[i]** 2
            norm_vector += val   
        return norm_vector**0.5


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
    
    def scale (self,scalar):
        scaled_matrix = []
        for a in range(self.dims[0]):
            scaled_matrix.append([])
            for b in range(self.dims[1]):
                val = self.matrix[a][b] * scalar 
                scaled_matrix[a].append(val)
        return scaled_matrix
    
    #to transpose 'tmatrix'
    def transpose(self):
        """Creates a new matrix with the rows and columns swapped"""
        trsp_matrix = []
        for w in range(self.dims[1]):
            trsp_matrix.append([])
            for q in range(self.dims[0]):
               trsp_matrix[w].append(self.matrix[q][w])
        return trsp_matrix

    def mul(self,tmatrix):
        """
        Matrix multiplication, two matrices
        Parameters: 
            tmatrix (self.matrix): the second matrix
        Returns: 
            The list of the new matrix after multiplication
        """
        mul_matrix = []
        for i in range(self.dims[0]): 
            mul_matrix.append([]) #creates the same number of rows as the first matrix
            for e in range(tmatrix.dims[1]): 
                v1 = Vector(self.matrix[i])
                v2 = Vector(tmatrix.transpose()[e])
                val = v1.dot(v2)
                mul_matrix[i].append(val) #appending a result for each column of the second matrix
        return mul_matrix

class FMatrix(Matrix):
    """child class to make more appeling the output"""
    def __init__(self,matrix,dims):
        super().__init__(matrix,dims)
    def fancy(self,target): #put separators between rows
        style = [str(a) for a in target]
        separator = "\n"
        style_output = separator.join(style)
        return style_output
    def add(self,tmatrix):
        add_matrix = self.fancy(super().add(tmatrix))
        return add_matrix    
    def mul(self,tmatrix):
        mul_matrix = self.fancy(super().mul(tmatrix))
        return mul_matrix
    def scale(self,scalar):
        scale_matrix = self.fancy(super().scale(scalar))
        return scale_matrix


