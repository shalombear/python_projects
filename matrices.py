#To Do:
#   add Vector methods
#   update docstrings
#   time methods
#   create Matrix class


"""
module covering the basic operations of linear algebra
    classes:
        Vector -- vectors in Euclidean space
            methods:
                __init__ -- instantiate a vector in Euclidean space
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
                    
"""

#importing libraries
import otoodles
import acceptors as acc

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
                    dotprod (number)
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
        rep = "[  "
        for num in self.array:
            rep += str(num)+"\t"
        rep = rep[:-1]
        rep += "  ]"
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

    def dot_product(self, other):
        if self.size != other.size:
            return None
        else:
            dotprod = 0
            for i in range(self.size):
                dotprod += self.array[i]*other.array[i]
            dotprod = sqrt(dotprod)
            return dotprod
        
        
        
