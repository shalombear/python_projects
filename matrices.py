"""
module covering the basic operations of linear algebra
    classes:
        vect -- vectors in Euclidean space
            methods:
                __init__ -- instantiate a vector in Euclidean space
                __repr__ -- 
                __add__ -- 
"""

#importing libraries
import otoodles
import acceptors as acc

#this function/class will be used a lot
from otoodles import D

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
    """

    #instantiation
    def __init__(self, entry=None):
        """
        instantiate a vector in Euclidean space
            parameters:
                entry (None or str='manual' or list)
            
        
        """

        #a vector is a list
        #default creation is the zero vector.
        self.size = 
        self.array = [0 for i in range(size)]
        if entry is None:
            for i in range(size)
        
        
