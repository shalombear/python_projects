#To Do:
#   add Vector methods
#   update docstrings
#   time methods
#   create Matrix class
#   create class and functionality for underlying field


"""
module covering the basic operations of linear algebra
    classes:
        Vector -- vectors in Euclidean space
            attributes:
                size (int) [size > 0]
                length (float)
                array (list)
            methods:
                __init__ -- instantiate a vector in Euclidean space
                    parameters:
                        entry (list)
                __repr__ -- representing the vector as a bracketed row
                        returns:
                            rep (str)
                __add__ -- vector addition
                    parameters:
                        other (Vector)
                    returns:
                        sum_vect (Vector)
                __sub__ -- vector subtraction
                    parameters:
                        other (Vector)
                    returns:
                        diff_vect (Vector)
                __eq__ -- vectors are equal if all their components are equal
                    parameters:
                        other (Vector)
                    returns
                        equal (bool)
                __rmul__ -- scalar multiplication
                    parameters:
                        scalar (float)
                    returns:
                        scaled_vect (Vector)
                dot_product -- dot product of two vectors
                    parameters:
                        other (Vector)
                    returns:
                        dot_product (float)
                angle -- angle between two vectors
                    parameters:
                        other (Vector)
                    returns:
                        theta (float) [measured in radians]
                        
                    
"""

#importing libraries
import math
import otoodles
import acceptors as acc
import fractions

#these functions and classes will be used a lot
from otoodles import D
from math import sqrt

#define the vector class
class Vector:
    """
    vector in Euclidean Space
        attributes:
            size -- the number of components in the vector
            length -- 
        methods:
            __init__ -- instantiate a vector in Euclidean space
                parameters:
                    entry (None or str='manual' or list)
            __repr__
            __add__
                parameters:
                    other (Vector)
                returns:
                    sum_vect (vector)
                
            dot_product --
                parameters:
                    other (Vector)
                returns:
                    dot_product (float)
    """

    #instantiation
    def __init__(self, entry):
        """
        instantiate a vector in Euclidean space
            parameters:
                entry (list)
            
        """

        #a vector is a list
        self.size = len(entry)
        self.array = entry
        self.length = self.dot_product(self)

    def __repr__(self):
        rep = "<"
        for num in self.array:
            worker = " {}  ".format(num)
            rep += worker
        rep = rep[:-1]
        rep += ">"
        return rep

    def __add__(self, other):
        if self.size != other.size:
            return None
        else:
            sum_entry = []
            for i in range(self.size):
                sum_entry.append(self.array[i] + other.array[i])
            sumvect = Vector(sum_entry)
            return sumvect

    def __sub__(self, other):
        if self.size != other.size:
            return None
        else:
            diff_entry = []
            for i in range(self.size):
                diff_entry.append(self.array[i] - other.array[i])
            diff_vect = Vector(diff_entry)
            return diff_vect

    def __eq__(self, other):
        if self.size != other.size:
            return False
        for i in range(self.size):
            if self.array[i] != other.array[i]:
                return False
        return True

    def __rmul__(self, scalar):
        scaled_entry = []
        for i in range(self.size):
            scaled_entry.append(scalar * self.array[i])
        scaled_vect = Vector(scaled_entry)
        return scaled_vect

    def dot_product(self, other):
        if self.size != other.size:
            return None
        else:
            worker = 0
            for i in range(self.size):
                worker += self.array[i] * other.array[i]
            dot_product = sqrt(worker)
            return dot_product

    def angle(self, other, unit='radians'):
        if self.size != other.size:
            return None
        else:
            theta = math.acos(self.dot_product(other) / (self.length * other.length))
            if 
            return theta
        
        
