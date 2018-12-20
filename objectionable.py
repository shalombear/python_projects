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
            
#the Node class will be used to implement data structures
class Node:
    """
    a node in a linked list
        attributes:
            value (any type)
            link_node (Node or None) [default=None]
        methods:
            __init__ -- instantiate a Node object
                parameters:
                    value (any)
                    link_node (None or None) [default=None]
            __repr__ -- represent the object as a string
                returns:
                    rep (str)
            set_link -- set a link node
                parameters:
                    link_node (Node)
            get_link -- retrieve a link node
                returns:
                    link_node (Node)
            get_value -- retrieve the value from a node
                returns:
                    value (any type)
    """

    #instantiation
    def __init__(self, value, link_node=None):
        """
        instantiate a node object
            parameters:
                value (any type)
                link_node (Node or None) [default=None]
        """

        #assigning attributes
        self.value = value
        self.link_node = link_node

    #representation
    def __repr__(self):
        """
        string representation of the Node object
            returns:
                rep (str)
        """

        if self.link_node is None:
            linker = '(unlinked node)'
        else:
            linker = self.link_node.value
        rep = "Data: \t{}\nLink: \t{}".format(self.value, linker)
        return rep

    #linking nodes
    def set_link(self, link_node):
        """
        assign a link to a node
            parameters:
                link_node (Node)
        """
        
        self.link_node = link_node

    #retrieving linked node
    def get_link(self):
        """
        retrieve a link node
            returns:
                link_node (Node)
        """

        return self.link_node

    #retrieving node's stored value
    def get_value(self):
        """
        retrieve the value from a node
            returns:
                value (any type)
        """

        return self.value


class LinkedList:
    """
    implementation of the linked list data structure
        attributes:
            head (Node)
        methods:
            __init__ -- instantiation
                parameters:
                    value (any type) [default=None]
            __repr__ -- string representation
                returns:
                    rep (str)
            insert_head -- add a new head node
                parameters:
                    new_value
        """

    #instantiation
    def __init__(self, value=None):
        """
        instantiate a linked list
            parameters:
                value (any type) [default=None]
        """

        #the value passed in is used to create the head node
        self.head = Node(value)

    #representation
    def __repr__(self):
        """
        represent the object as a string
            returns:
                rep (str)
        """

        #start with an empty string
        rep = ""

        #beginning at the head
        current_node = self.head

        #iterate through the list and concatenate the values
        while current_node:
            if current_node.get_value() != None:
                rep += str(current_node.get_value())
                rep += "\n"
                current_node = current_node.get_link()
        return rep

    #adding a new head to the list
    def insert_head(self, new_value):
        """
        add a new head node to the list
            parameters:
                new_value (any type)
        """

        #instantiate the new  node
        new_node = Node(new_value)

        #link to the current head node
        new_node.set_link(self.head)

        #assign as the new head
        self.head = new_node

class Stack:
    """
    a LIFO stack
        attributes:
            top_item (any type)
        methods:
            __init__ -- instantiation
                parameters:
                    bottom_value (any type) [default=None]
            is_empty --
                returns:
                    is (bool)
            push -- add a value to the top of the stack
                parameters:
                    value (any type)
            pop -- remove and return top item from stack
                returns:
                    value (any type)

            peek
                returns:
                    value (any type)
    """

    #instantiation
    def __init__(self, bottom_value=None):
        """
        instantiate a LIFO stack
            parameters:
                bottom_value (any type) [default=None]
        """
        
        #this attribute represents the top item
        #the value _init_ially stored is the first_in element,
        #the bottom of the stack

        #stack can be instantiated with one object
        if bottom_value is not None:
            self.top_item = Node(bottom_value)

        #or empty
        else:
            self.top_item = None

    def is_empty(self):

        empty = self.top_item is None
        return empty

    #push method
    def push(self, value):
        """
        add a value to the top of the stack
            parameters:
                value (any type)
        """

        #create node
        node = Node(value)

        #link to top
        node.set_link(self.top_item)

        #node is new top
        self.top_item = node

    #pop method
    def pop(self):
        """
        remove and return top item on stack
            returns:
                value (any type)
        """

        #call the value if it exists
        if not self.is_empty():
            value = self.top_item.value

        #otherwise print error message
        else:
            print("Stack is empty")
            return None

        #set new top item and return value
        self.top_item = self.top_item.link_node
        return value

    #peek method
    def peek(self):
        """
        call top value without removing from stack
            returns:
                value (any type)
        """

        #call the value if it exists
        if not self.is_empty():
            value = self.top_item.value
            return value

        #otherwise print error message
        else:
            print("Stack is empty")
            
            
class MeasuredStack(Stack):
    """
    a LIFO stack with a counter and an optional maximum size
        inheritance:
            Stack
        attributes:
            size (int >= 0)
            limit (int > 0 or None)
        methods:
            __init__ -- instantiation
                parameters:
                    bottom_value (any type) [default=None]
                    limit (int > 0) [default=None]
    """

    #instantiation
    def __init__(self, bottom_value=None, limit=None):
        """
        instantiate a measured stack object
            parameters:
                bottom_value (any type) [default=None]
                limit (int > 0) [default=None]
        """

        #a stack can be instantiated empty
        if bottom_value is None:
            self.size = 0

        #or with a single object
        else:
            self.size = 1

        #call the parent method to instantiate
        super().__init__(bottom_value)

        #set the limit
        self.limit = limit

    def has_space(self):
        """
        check if the stack is not full
            returns:
                has (bool)
        """

        has = self.size < self.limit or self.limit is None

        return has
        
    def push(self, value):
        """
        add a value to the top of the stack
            parameters:
                value (any type)
        """

        #the stack must not be full
        if self.has_space():
            super().push(value)
            self.size += 1
        else:
            print("Stack is full")

    def pop(self):
        """
        return top value and remove from stack
            returns:
                value (any type)
        """

        #decrement size and invoke the parent method
        if self.size > 0:
            self.size -= 1
        value = super().pop()

        return value


class Queue:
    """
    a FIFO queue
        attributes:
            head (Node or None)
            tail (Node or None)
            cap (int > 0 or None)
            size (int >= 0)
        methods:
            __init__ -- instantiation
                parameters:
                    cap (int > 0 or None) [default=None]
    """

    #instantiation
    def __init__(self, cap=None):
        """instantiate a queue"""

        #line is intitialized in empty state
        self.head = None
        self.tail = None
        self.size = 0
        self.cap = cap

    def is_empty(self):

        empty = self.size == 0
        return empty

    def is_full(self):
        
        full = self.size == self.cap and self.cap is not None
        return full

    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            return self.head.value

    def enqueue(self, value):

        if not self.is_full():
            new_item = Node(value)
            print("Adding {} to the queue".format(new_item.value))

            if self.is_empty():
                self.head = new_item

            else:
                self.tail.set_link(new_item)

            self.tail = new_item
            self.size += 1

        else:
            print("Queue is full")

    def dequeue(self):

        if not self.is_empty():
            value = self.head.value
            self.head = self.head.get_link()
            self.size -= 1
            return value

        else:
            print("Queue is empty")

#node objects for use in tree structures
class TreeNode:
    """
    a node in a tree
        attributes:
            value (any type)
            children (list)
        methods:
            __init__ -- instantiation
                parameters:
                    value (any type)
            add_child -- add a child to the node
                parameters:
                    value (any type)
            remove_child -- remove a child from the node
                parameters:
                    child (TreeNode)
    """

    def __init__(self, value):
        """
        instantiate a TreeNode object
            parameters:
                value (any type)
        """

        self.value = value
        self.children = []

    def __repr__(self, level=0):
        """
        represent the node's subtree as a string
            returns:
                rep (str)
                level (int >= 0) [default=0]
        """

        worker = ""
        worker += "-->" * level
        worker += str(self.value)
        worker += "\n"

        #recursion
        for child in self.children:
            worker += child.__repr__(level+1)

        rep = worker
        return rep

    def add_child(self, child):
        """
        add a child node
            parameters:
                child (TreeNode)
        """

        self.children.append(child)

    def remove_child(self, child):
        """
        remove a child node
            parameters:
                child (TreeNode)
        """

        new_children = [obj for obj in self.children if obj != child]
        self.children = new_children

    def traverse(self):
        """iterate through the node's subtree in a depth-first manner"""

        lister = []
        lister.append(self.value)

        for child in self.children:
            lister += child.traverse()

        return lister
