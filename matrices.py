"""
A module covering the basic operations of linear algebra
    classes:
        vect -- vectors in Euclidean space
            methods:
                __init__ -- initialization can be manual or computer-generated
                    args:
                        inputs (list) [default: 'manual' (str)]
                length
"""

#importing libraries
import otoodles
import acceptors as acc

#this function/class will be used a lot
from otoodles import D

#define the vector class
class vect:

    #initialization is manual or computer-generated
    def __init__(self, inputs='manual'):
        if inputs == 'manual':
            pass
