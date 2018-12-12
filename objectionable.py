"""
Classes and functions for mathematical objects of all types
    classes:
        Vertex -- vertices of a graph
            attributes:
                value (any)
                edges (list)
            methods:
                __init__ -- instantiation
                    parameters:
                        value (any) [default=None]
                __repr__ -- string representation
                    returns:
                        rep (str)
                __eq__ -- two vertices are equal if their values and all their edges are equal
                    parameters:
                        other (Vertex)
                    returns:
                        equal (bool)
                add_edge -- adding an edge to a vertex
                    parameters:
                        other (Vertex)

        Graph -- a collection of Vertex objects
            attributes:
                vertices (list)
                edges (list)
            methods:
                __init__ -- instantiation
                    parameters:
                        vertices (list)
                add_vertex -- adding a vertex to the graph
                    parameters:
                        vertex (Vertex)
                add_edge -- adding an edge to the graph
                    parameters:
                        v1 (Vertex)
                        v2 (Vertex)

"""

#importing libraries
import math
import random

#importing functions
from math import sqrt
from otoodles import D

#graphs
#the graph vertex class
class Vertex:
    """
    vertices of a graph
        attributes:
            edges (list)
        methods:
            __init__ -- instantiation
            __repr__ -- string representation
            add_edge -- adding an edge to the graph
                parameters:
                    other (Vertex)
    """

    #instantiation
    def __init__(self, value=None):
        """instantiate a vertex of a graph"""
        self.value = value

        #object instantiates with an empty container for the edges
        self.edges = []

    #string representation
    def __repr__(self):
        """string representation of a graph vertext"""

        #need to put more thought into how this is going down
        rep = str(self.value)
        return rep

    #method to add an edge to the graph
    def add_edge(self, other):
        """
        add an edge to the graph between self and other
            parameters:
                other (Vertex)
        """
        if other not in self.edges:
            self.edges.append(other)

        if self != other:
            other.edges.append(self)

class Graph:
    """
    A collection of Vertex objects
        attributes:
            vertices (list)
            edges (list)
        methods:
            __init__ -- instantiation
                parameters:
                    vertices (list)
            add_vertex -- adding a vertex to the graph
                parameters:
                    vertex (Vertex)
            add_edge -- adding an edge to the graph
                parameters:
                    v1 (Vertex)
                    v2 (Vertex)
    """

    def __init__(self, vertices):
        self.vertices = vertices
        edgelist = []
        for vertex in vertices:
            for edge in vertex.edges:
                if [vertex, edge] not in edgelist and [edge, vertex] not in edgelist:
                    edgelist.append(vertex, edge)
            
