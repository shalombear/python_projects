"""classes and functions for mathematical objects of all types

classes:
    Node -- a node in a linked list
        attributes:
            value (any type)
            link_node (Node or None) [default=None]
        methods:
            __init__ -- instantiate a Node object
                args:
                    value (any)
                    link_node (None or None) [default=None]
            __repr__ -- represent the object as a string
                returns:
                    rep (str)
            set_link -- set a link node
                args:
                    link_node (Node)
            get_link -- retrieve a link node
                returns:
                    link_node (Node)
            get_value -- retrieve the value from a node
                returns:
                    value (any type)

    LinkedList -- a linked list data structure
        attributes:
            head (Node)
        methods:
            __init__ -- instantiation
                args:
                    value (any type) [default=None]
            __repr__ -- string representation
                returns:
                    rep (str)
            insert_head -- add a new head node
                args:
                    new_value

    Stack -- a LIFO stack
        attributes:
            top_item (any type)
        methods:
            __init__ -- instantiation
                args:
                    bottom_value (any type) [default=None]
            is_empty -- helper method checks if stack is empty
                returns:
                    empty (bool)
            push -- add a value to the top of the stack
                args:
                    value (any type)
            pop -- remove and return top item from stack
                returns:
                    value (any type)
            peek
                returns:
                    value (any type)

    MeasuredStack -- a LIFO stack with a counter and an optional maximum size
        inheritance:
            Stack
        attributes:
            size (int >= 0)
            limit (int > 0 or None)
        methods:
            __init__ -- instantiation
                args:
                    bottom_value (any type) [default=None]
                    limit (int > 0) [default=None]
            has_space -- check if the stack is not full
                returns:
                    has (bool)
            push -- add a value to the top of the stack
                args:
                    value (any type)
            pop -- remove and return top item from stack
                returns:
                    value (any type)
            peek
                returns:
                    value (any type)

    Queue -- a FIFO queue
        attributes:
            head (Node or None)
            tail (Node or None)
            cap (int > 0 or None)
            size (int >= 0)
        methods:
            __init__ -- instantiation
                args:
                    cap (int > 0 or None) [default=None]
            __repr__ -- string representation
                returns:
                    rep (str)
            is_empty -- check if the string is empty
                returns:
                    empty (bool)
            is_full -- check if queue is full
                returns:
                    full (bool)
            peek -- return the leading value of the queue
                returns:
                    val (any type)
            enqueue -- add a node to the queue
                args:
                    value(any type)
            dequeue -- remove head and return
                returns:
                    value (any type)

    TreeNode -- a node in a tree
        attributes:
            value (any type)
            children (list)
        methods:
            __init__ -- instantiation
                args:
                    value (any type)
            __repr__ -- represent the tree as a string
                args:
                    level (int >= 0) [default=0]
                returns:
                    rep (str)
            add_child -- add a child to the node
                args:
                    child (TreeNode)
            remove_child -- remove a child from the node
                args:
                    child (TreeNode)
            traverse -- iterate through the node's subtree depth-first
                returns:
                    lister (list)

    Heap -- an ordered binary tree
        attributes:
            heap_list (list)
            count (int >= 0)
        methods:
            __init__ -- instantiate a Heap object
            is_empty -- check if heap is empty
                returns:
                    empty (bool)
            parent_idx -- find the parent index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            left_child_idx -- find the left child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            right_child_idx -- find the right child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            add -- add an item to the heap
                args:
                    element (any type)
            peek --return a copy of the top element
                returns:
                    val (any type)
            pop -- remove and return top element from heap
                returns:
                    val (any type)

    MinHeap -- an ordered minimum heap
        attributes:
            heap_list (list)
            count (int >= 0)
        methods:
            __init__ -- instantiate a MinHeap object
            is_empty -- check if heap is empty
                returns:
                    empty (bool)
            parent_idx -- find the parent index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            left_child_idx -- find the left child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            right_child_idx -- find the right child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            get_smaller_child_idx -- find the smaller child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            add -- add an item to the heap
                args:
                    element (any type)
            heapify_up -- bubble up from bottom to order heap
            peek -- return a copy of the top element
                returns:
                    val (any type)
            pop -- remove and return minimum element from heap and resort
                returns:
                    mini (any type)
            heapify_down -- bubble down from top to restore order

    MaxHeap -- an ordered maximum heap
        attributes:
            heap_list (list)
            count (int >= 0)
        methods:
            __init__ -- instantiate a MinHeap object
            is_empty -- check if heap is empty
                returns:
                    empty (bool)
            parent_idx -- find the parent index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            left_child_idx -- find the left child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            right_child_idx -- find the right child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            get_larger_child_idx -- find the larger child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            add -- add an item to the heap
                args:
                    element (any type)
            heapify_up -- bubble up from bottom to order heap
            peek -- return a copy of the top element
                returns:
                    val (any type)
            pop -- remove and return maximum element from heap and resort
                returns:
                    maxi (any type)
            heapify_down -- bubble down from top to restore order

    Vertex -- vertex of a graph
        attributes:
            value (any)
            edges (dict)
        methods:
            __init__ -- instantiation
                args:
                    value (any)
            get_edges -- retrieve a list of connected vertices
                returns:
                    edges (list)
            __repr__ -- string representation
                returns:
                    rep (str)
            add_edge -- adding an edge to a vertex
                args:
                    other (Vertex)

    Graph -- a collection of Vertex objects
        attributes:
            vertices (dict)
            directed (bool)
        methods:
            __init__ -- instantiation
                args:
                    directed (bool) [default=False]
            __repr__ -- string representation
                returns:
                    rep (str)
            add_vertex -- add a vertex to the graph
                args:
                    vertex (Vertex)
            add_edge -- add an edge to the graph
                args:
                    v1 (Vertex)
                    v2 (Vertex)
                    
    Proposition -- statement in a propositional calculus
        attributes:
            statement (str)
            truth (bool or None) [default=None]
        methods:
            __init__ -- instantiation
                args:
                    statement (str)
                    truth (bool or None) [default=None]
            __repr__ -- representation
                returns:
                    rep (str)
            __neg__ -- negation
                returns
                    negation (Proposition)
            __and__ -- conjunction
                args:
                    other (Proposition)
                returns
                    conjunction (Proposition)
            __or__ -- disjunction
                args:
                    other (Proposition)
                returns
                    disjunction (Proposition)
            __rshift__ -- implication
                args:
                    other (Proposition)
                returns
                    implication (Proposition)

    FuzzyProposition -- statement in a fuzzy propositional calculus
        inheritance:
            Proposition
        attributes:
            statement (str)
            truth (0 <= float <=1 or None) [default=None]
        methods:
            __init__ -- instantiation
                args:
                    statement (str)
                    truth (0 <= float <= 1 or None) [default=None]
            __repr__ -- representation
                returns:
                    rep (str)
            __neg__ -- negation
                returns
                    negation (FuzzyProposition)
            __and__ -- conjunction
                args:
                    other (FuzzyProposition)
                returns
                    conjunction (FuzzyProposition)
            __or__ -- disjunction
                args:
                    other (FuzzyProposition)
                returns
                    disjunction (FuzzyProposition)
            __rshift__ -- implication
                args:
                    other (FuzzyProposition)
                returns
                    implication (FuzzyProposition)

"""

# importing libraries
import math
import random

# importing functions
from math import sqrt
from otoodles import D

            
# the Node class is used to implement data structures
class Node:
    """a node in a linked list
        attributes:
            value (any type)
            link_node (Node or None) [default=None]
        methods:
            __init__ -- instantiate a Node object
                args:
                    value (any)
                    link_node (None or None) [default=None]
            __repr__ -- represent the object as a string
                returns:
                    rep (str)
            set_link -- set a link node
                args:
                    link_node (Node)
            get_link -- retrieve a link node
                returns:
                    link_node (Node)
            get_value -- retrieve the value from a node
                returns:
                    value (any type)
    """

    # instantiation
    def __init__(self, value, link_node=None):
        """instantiate a node object
            args:
                value (any type)
                link_node (Node or None) [default=None]
        """

        #assigning attributes
        self.value = value
        self.link_node = link_node

    # representation
    def __repr__(self):
        """string representation of the Node object
            returns:
                rep (str)
        """

        if self.link_node is None:
            linker = '(unlinked node)'
        else:
            linker = self.link_node.value
        rep = "Data: \t{}\nLink: \t{}".format(self.value, linker)
        return rep

    # linking nodes
    def set_link(self, link_node):
        """assign a link to a node
            args:
                link_node (Node)
        """
        
        self.link_node = link_node

    # retrieving linked node
    def get_link(self):
        """retrieve a link node
            returns:
                link_node (Node)
        """

        return self.link_node

    # retrieving node's stored value
    def get_value(self):
        """retrieve the value from a node
            returns:
                value (any type)
        """

        return self.value

# linked list data structure
class LinkedList:
    """implementation of linked list data structure
        attributes:
            head (Node)
        methods:
            __init__ -- instantiation
                args:
                    value (any type) [default=None]
            __repr__ -- string representation
                returns:
                    rep (str)
            insert_head -- add a new head node
                args:
                    new_value
        """

    # instantiation
    def __init__(self, value=None):
        """instantiate a linked list
            args:
                value (any type) [default=None]
        """

        # the value passed in is used to create the head node
        self.head = Node(value)

    # representation
    def __repr__(self):
        """represent the object as a string
            returns:
                rep (str)
        """

        # start with an empty string
        rep = ""

        # beginning at the head
        current_node = self.head

        # iterate through the list and concatenate the values
        while current_node:
            if current_node.get_value() != None:
                rep += str(current_node.get_value())
                rep += "\n"
                current_node = current_node.get_link()
        return rep

    # adding a new head to the list
    def insert_head(self, new_value):
        """add a new head node to the list
            args:
                new_value (any type)
        """

        # instantiate the new  node
        new_node = Node(new_value)

        # link to the current head node
        new_node.set_link(self.head)

        # assign as the new head
        self.head = new_node

class Stack:
    """a LIFO stack
        attributes:
            top_item (any type)
        methods:
            __init__ -- instantiation
                args:
                    bottom_value (any type) [default=None]
            is_empty -- helper method checks if stack is empty
                returns:
                    empty (bool)
            push -- add a value to the top of the stack
                args:
                    value (any type)
            pop -- remove and return top item from stack
                returns:
                    value (any type)
            peek -- look at top of stack
                returns:
                    value (any type)
    """

    # instantiation
    def __init__(self, bottom_value=None):
        """instantiate a LIFO stack
            args:
                bottom_value (any type) [default=None]
        """
        
        # this attribute represents the top item
        # the value _init_ially stored is the first_in element,
        # the bottom of the stack

        # stack can be instantiated with one object
        if bottom_value is not None:
            self.top_item = Node(bottom_value)

        # or empty
        else:
            self.top_item = None

    def is_empty(self):
        """helper method checks if stack is empty
                returns:
                    empty (bool)
        """

        empty = self.top_item is None
        return empty

    # push method
    def push(self, value):
        """add a value to the top of the stack
            args:
                value (any type)
        """

        # create node
        node = Node(value)

        # link to top
        node.set_link(self.top_item)

        # node is new top
        self.top_item = node

    # pop method
    def pop(self):
        """remove and return top item on stack
            returns:
                value (any type)
        """

        # call the value if it exists
        if not self.is_empty():
            value = self.top_item.value

        # otherwise print error message
        else:
            print("Stack is empty")
            return None

        # set new top item and return value
        self.top_item = self.top_item.link_node
        return value

    # peek method
    def peek(self):
        """call top value without removing from stack
            returns:
                value (any type)
        """

        # call the value if it exists
        if not self.is_empty():
            value = self.top_item.value
            return value

        # otherwise print error message
        else:
            print("Stack is empty")
            
            
class MeasuredStack(Stack):
    """a LIFO stack with a counter and an optional maximum size
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
            has_space -- check if the stack is not full
                returns:
                    has (bool)
            push -- add a value to the top of the stack
                args:
                    value (any type)
            pop -- remove and return top item from stack
                returns:
                    value (any type)
            peek
                returns:
                    value (any type)
    """

    # instantiation
    def __init__(self, bottom_value=None, limit=None):
        """instantiate a measured stack object
            args:
                bottom_value (any type) [default=None]
                limit (int > 0) [default=None]
        """

        # a stack can be instantiated empty
        if bottom_value is None:
            self.size = 0

        # or with a single object
        else:
            self.size = 1

        # call the parent method to instantiate
        super().__init__(bottom_value)

        # set the limit
        self.limit = limit

    def has_space(self):
        """check if the stack is not full
            returns:
                has (bool)
        """

        has = self.size < self.limit or self.limit is None

        return has
        
    def push(self, value):
        """add a value to the top of the stack
            parameters:
                value (any type)
        """

        # the stack must not be full
        if self.has_space():
            super().push(value)
            self.size += 1
        else:
            print("Stack is full")

    def pop(self):
        """return top value and remove from stack
            returns:
                value (any type)
        """

        # decrement size and invoke the parent method
        if self.size > 0:
            self.size -= 1
        value = super().pop()

        return value


class Queue:
    """a FIFO queue
        attributes:
            head (Node or None)
            tail (Node or None)
            cap (int > 0 or None)
            size (int >= 0)
        methods:
            __init__ -- instantiation
                args:
                    cap (int > 0 or None) [default=None]
            __repr__ -- string representation
                returns:
                    rep (str)
            is_empty -- check if the string is empty
                returns:
                    empty (bool)
            is_full -- check if queue is full
                returns:
                    full (bool)
            peek -- return the leading value of the queue
                returns:
                    val (any type)
            enqueue -- add a node to the queue
                args:
                    value(any type)
            dequeue -- remove head and return
                returns:
                    value (any type)
    """

    # instantiation
    def __init__(self, cap=None):
        """instantiate a queue
            args:
                cap (int > 0 or None) [default=None]
        """

        # line is intitialized in empty state
        self.head = None
        self.tail = None
        self.size = 0
        self.cap = cap

    # string representation
    def __repr__(self):
        """represent queue as a string
            returns:
                rep (str)
        """

        # constructing the representation
        if self.is_empty():
            rep = "The queue is empty"
        else:
            rep = 'Size: {0}\nHead: {1}'.format(self.size, self.head.value)

        return rep

    # helper method checks if queue is empty
    def is_empty(self):
        """check if the string is empty
            returns:
                empty (bool)"""

        empty = self.size == 0

        return empty

    # helper method checks if queue is full
    def is_full(self):
        """check if queue is full
            returns:
                full (bool)
        """
        
        full = self.size == self.cap and self.cap is not None

        return full

    # looking at the head of the queue
    def peek(self):
        """return the leading value of the queue
            returns:
                val (any type)
        """
        
        if self.is_empty():
            val = None
        else:
            val =  self.head.value

        return val

    # adding an item to the queue
    def enqueue(self, value):
        """add a node to the queue if possible
            args:
                value (any type)                
        """
        
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

    # removing an item from the queue
    def dequeue(self):
        """remove head and return
            returns:
                value (any type)
        """

        if not self.is_empty():
            value = self.head.value
            self.head = self.head.get_link()
            self.size -= 1
            return value

        else:
            return None

# node objects for use in tree structures
class TreeNode:
    """a node in a tree
        attributes:
            value (any type)
            children (list)
        methods:
            __init__ -- instantiation
                args:
                    value (any type)
            __repr__ -- represent the tree as a string
                args:
                    level (int >= 0) [default=0]
                returns:
                    rep (str)
            add_child -- add a child to the node
                args:
                    child (TreeNode)
            remove_child -- remove a child from the node
                args:
                    child (TreeNode)
    """

    def __init__(self, value):
        """instantiate a TreeNode object
            args:
                value (any type)
        """

        self.value = value
        self.children = []

    def __repr__(self, level=0):
        """represent the tree as a string
            args:
                level (int >= 0) [default=0]
            returns:
                rep (str)
        """

        # building the string
        rep = ""
        rep += "-->" * level
        rep += str(self.value) + "\n"
        
        # recursive calls
        for child in self.children:
            rep += child.__repr__(level+1)

        return rep


    def add_child(self, child):
        """add a child node
            args:
                child (TreeNode)
        """

        self.children.append(child)

    def remove_child(self, child):
        """remove a child node
            args:
                child (TreeNode)
        """

        new_children = [obj for obj in self.children if obj != child]
        self.children = new_children

    def traverse(self):
        """iterate through the node's subtree depth-first
            returns:
                lister (list)
        """

        lister = []
        lister.append(self.value)

        for child in self.children:
            lister += child.traverse()

        return lister

class Heap:
    """an ordered binary tree
        attributes:
            heap_list (list)
            count (int >= 0)
        methods:
            __init__ -- instantiate a Heap object
            is_empty -- check if heap is empty
                returns:
                    empty (bool)
            parent_idx -- find the parent index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            left_child_idx -- find the left child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            right_child_idx -- find the right child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            add -- add an item to the heap
                args:
                    element (any type)
            peek --return a copy of the top element
                returns:
                    val (any type)
            pop -- remove and return top element from heap
                returns:
                    val (any type)
    """

    # instantiation
    def __init__(self):
        """instantiate a heap object
        """

        # declaring attributes
        # heap is stored as a list with a sentinel value
        self.heap_list = [None,]
        self.count = 0

    # Helper methods
    def is_empty(self):
        """check if heap is empty
            returns:
                empty (bool)
        """

        empty = self.count == 0
        return empty
    
    def parent_idx(self, idx):
        """find the parent index of an element
            args:
                idx (int > 0)
            returns:
                idx (int > 0)
        """

        idx //= 2
        return idx

    def left_child_idx(self, idx):
        """find the left child index of an element
            args:
                idx (int > 0)
            returns:
                idx (int > 0)
        """

        idx *= 2
        return idx

    def right_child_idx(self, idx):
        """find the right child index of an element
            args:
                idx (int > 0)
            returns:
                idx (int > 0)
        """

        idx *= 2 + 1
        return idx

    # adding an element to the heap
    def add(self, element):
        """add an element to the heap
            args:
                element (any type)
        """

        self.count += 1
        self.heap_list.append(element)

    # peeking at the top of the heap
    def peek(self):
        """return a copy of the top element
            returns:
                val (any type)
        """

        # checking if heap is empty
        if self.is_empty():
            print("Heap is empty")
            return None

        # otherwise return top value without removing
        else:
            val = self.heap_list[1]
            return val

    # popping off the top value from the heap
    # heap properties may not be maintained if used without heapify down
    def pop(self):
        """remove and return top element from heap
            returns:
                val (any type)
        """

        # checking if heap is empty
        if self.is_empty():
            print("Heap is empty")
            return None

        # otherwise swap top item with last item and return
        else:
            val = self.heap_list[1]
            self.heap_list[1] = self.heap_list[-1]
            self.heap_list.pop(-1)
            self.count -= 1

        return val

class MinHeap(Heap):
    """an ordered minimum heap
        attributes:
            heap_list (list)
            count (int >= 0)
        methods:
            __init__ -- instantiate a MinHeap object
            is_empty -- check if heap is empty
                returns:
                    empty (bool)
            parent_idx -- find the parent index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            left_child_idx -- find the left child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            right_child_idx -- find the right child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            get_smaller_child_idx -- find the smaller child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            add -- add an item to the heap
                args:
                    element (any type)
            heapify_up -- bubble up from bottom to order heap
            peek -- return a copy of the top element
                returns:
                    val (any type)
            pop -- remove and return minimum element from heap and resort
                returns:
                    mini (any type)
            heapify_down -- bubble down from top to restore order
    """

    # helper method to find the index of the smaller of an element's children
    def get_smaller_child_idx(self, idx):
        """get_smaller_child_idx -- find the smaller child index of an element
            args:
                idx (int > 0)
            returns:
                idx (int > 0)
        """

        left_child = self.heap_list[self.left_child_idx(idx)]

        try:
            right_child = self.heap_list[self.right_child_idx(idx)]
        except IndexError:
            return self.left_child_idx(idx)

        else:
            if left_child < right_child:
                return self.left_child_idx(idx)
            else:
                return self.right_child_idx(idx)

    # adding an element to the heap
    def add(self, element):
        """add an element to the heap
            args:
                element (any type)
        """

        # call superclass method and reorder
        super().add(element)
        self.heapify_up()

    # heapify up method
    def heapify_up(self):
        """bubble up from bottom to restore order
        """

        # setting the index
        idx = self.count

        # perform repeated checkswaps until list is ordered
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]

            # check and swap
            if parent > child:
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child

            # reindex
            idx = self.parent_idx(idx)

    # pop with reorder
    def pop(self):
        """remove and return minimum element from heap and resort
            returns:
                mini (any type)
        """

        mini = super().pop()
        self.heapify_down()

        return mini

    # heapify down method
    def heapify_down(self):
        """bubble down from top to restore order
        """

        # setting the index
        idx = 1

        # perform repeated checkswaps until list is ordered
        while self.left_child_idx(idx) <= self.count:
            smaller_child_idx = self.get_smaller_child_idx(idx)
            child = self.heap_list[smaller_child_idx]
            parent = self.heap_list[idx]

            # check and swap
            if parent > child:
                self.heap_list[idx] = child
                self.heap_list[smaller_child_idx] = parent

            # reindex
            idx = smaller_child_idx

class MaxHeap(Heap):
    """an ordered maximum heap
        attributes:
            heap_list (list)
            count (int >= 0)
        methods:
            __init__ -- instantiate a MinHeap object
            is_empty -- check if heap is empty
                returns:
                    empty (bool)
            parent_idx -- find the parent index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            left_child_idx -- find the left child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            right_child_idx -- find the right child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            get_larger_child_idx -- find the larger child index of an element
                args:
                    idx (int > 0)
                returns:
                    idx (int > 0)
            add -- add an item to the heap
                args:
                    element (any type)
            heapify_up -- bubble up from bottom to order heap
            peek -- return a copy of the top element
                returns:
                    val (any type)
            pop -- remove and return maximum element from heap and resort
                returns:
                    maxi (any type)
            heapify_down -- bubble down from top to restore order
    """

    # helper method to find the index of the larger of an element's children
    def get_smaller_child_idx(self, idx):
        """get_larger_child_idx -- find the larger child index of an element
            args:
                idx (int > 0)
            returns:
                idx (int > 0)
        """

        left_child = self.heap_list[self.left_child_idx(idx)]

        try:
            right_child = self.heap_list[self.right_child_idx(idx)]
        except IndexError:
            return self.left_child_idx(idx)

        else:
            if left_child > right_child:
                return self.left_child_idx(idx)
            else:
                return self.right_child_idx(idx)

    # adding an element to the heap
    def add(self, element):
        """add an element to the heap
            args:
                element (any type)
        """

        # call superclass method and reorder
        super().add(element)
        self.heapify_up()

    # heapify up method
    def heapify_up(self):
        """bubble up from bottom to restore order
        """

        # setting the index
        idx = self.count

        # perform repeated checkswaps until list is ordered
        while self.parent_idx(idx) > 0:
            child = self.heap_list[idx]
            parent = self.heap_list[self.parent_idx(idx)]

            # check and swap
            if parent < child:
                self.heap_list[idx] = parent
                self.heap_list[self.parent_idx(idx)] = child

            # reindex
            idx = self.parent_idx(idx)

    # pop with reorder
    def pop(self):
        """remove and return maximum element from heap and resort
            returns:
                maxi (any type)
        """

        maxi = super().pop()
        self.heapify_down()

        return maxi

    # heapify down method
    def heapify_down(self):
        """bubble down from top to restore order
        """

        # setting the index
        idx = 1

        # perform repeated checkswaps until list is ordered
        while self.left_child_idx(idx) <= self.count:
            smaller_child_idx = self.get_smaller_child_idx(idx)
            child = self.heap_list[smaller_child_idx]
            parent = self.heap_list[idx]

            # check and swap
            if parent < child:
                self.heap_list[idx] = child
                self.heap_list[smaller_child_idx] = parent

            # reindex
            idx = smaller_child_idx

# graphs
# the graph vertex class
class Vertex:
    """vertex of a graph
        attributes:
            value (any)
            edges (dict)
        methods:
            __init__ -- instantiation
                args:
                    value (any)
            get_edges -- retrieve a list of connected vertices
                returns:
                    edges (list)
            __repr__ -- string representation
                returns:
                    rep (str)
            add_edge -- adding an edge to a vertex
                args:
                    other (Vertex)
    """

    # instantiation
    def __init__(self, value):
        """instantiate a vertex of a graph
            args:
                value (any)
        """

        # assigning attributes
        self.value = value

        # object instantiates with an empty container for the edges
        self.edges = {}

    # helper method to retrieve a vertex's edges
    def get_edges(self):
        """return a list of connected vertices
            returns:
                edges (list)
        """

        edges = list(self.edges.keys())
        return edges

    # string representation
    def __repr__(self):
        """string representation of a graph vertext
            returns:
                rep (str)
        """

        # a vertex is represented by its value and a list of its neighbors
        rep = str(self.value)
        rep += ":"
        for neighbor in self.get_edges():
            rep += " "+ str(neighbor.value) + ","
        rep = rep[:-1]
            
        return rep

    # adding an edge to connect to another vertex
    def add_edge(self, other):
        """add an edge connecting the vertex to another
            args:
                other (Vertex)
        """

        # adding other vertex to edges
        self.edges[other] = True

# graph class
class Graph:
    """a collection of Vertex objects
        attributes:
            vertices (dict)
            directed (bool)
        methods:
            __init__ -- instantiation
                args:
                    directed (bool) [default=False]
            __repr__ -- string representation
                returns:
                    rep (str)
            add_vertex -- add a vertex to the graph
                args:
                    vertex (Vertex)
            add_edge -- add an edge to the graph
                args:
                    v1 (Vertex)
                    v2 (Vertex)
    """

    # instantiation
    def __init__(self, directed=False):
        """instantiate a graph object
            args:
                directed (bool) [default=False]
        """

        # assigning attributes
        self.directed = directed

        # the graph's vertices are stored in a dictionary
        # key is vertex and value is a list of neighboring vertices
        self.vertices = {}

    # string representation
    def __repr__(self):
        """return string representation of graph object
            returns:
                rep (str)
        """

        rep = ""
        for vertex in self.vertices:
            rep += str(vertex) + "\n"

        rep = rep[:-1]

        return rep

    # adding a vertex to the graph
    def add_vertex(self, vertex):
        """add a vertex to the graph and use it to populate
            args:
                vertex (Vertex)
        """

        # if the vertex is already in the graph it is not overwritten
        if vertex not in self.vertices.keys():
            self.vertices[vertex] = []

        # using the added vertex to populate the graph
        # iterating through the connected vertices
        for neighbor in vertex.get_edges():

            # recursive call to populate dictionary with neighbor
            if neighbor not in self.vertices.keys():
                self.add_vertex(neighbor)

            # adding the edge to the graph
            self.add_edge(vertex, neighbor)

    # adding an edge to the graph and populating
    def add_edge(self, v1, v2):
        """add an edge to the graph
            args:
                v1 (Vertex)
                v2 (Vertex)
        """

        # populating graph dictionary with vertices
        for v in [v1, v2]:
            if v not in self.vertices.keys():
                self.vertices[v] = []

        # updating the graph dictionary
        if v2 not in self.vertices[v1]:
            self.vertices[v1].append(v2)
        
        # updating the vertex object
        v1.add_edge(v2)

        # reciprocating if graph is undirected
        if not self.directed and v1 not in self.vertices[v2]:
            self.add_edge(v2, v1)

class Proposition:
    """statement in a propositional calculus
        attributes:
            statement (str)
            truth (bool or None) [default=None]
        methods:
            __init__ -- instantiation
                args:
                    statement (str)
                    truth (bool or None) [default=None]
            __repr__ -- representation
                returns:
                    rep (str)
            __neg__ -- negation
                returns
                    negation (Proposition)
            __and__ -- conjunction
                args:
                    other (Proposition)
                returns
                    conjunction (Proposition)
            __or__ -- disjunction
                args:
                    other (Proposition)
                returns
                    disjunction (Proposition)
            __rshift__ -- implication
                args:
                    other (Proposition)
                returns
                    implication (Proposition)
    """

    # instantiation
    def __init__(self, statement, truth=None):
        """instantiate a statement in the propositional calculus
            args:
                statement (str)
                truth (bool or None) [default=None]
        """

        # assigning attributes
        self.statement = statement
        self.truth = truth

    # string representation
    def __repr__(self):
        """represent proposition as a string
            returns:
                rep (str)
        """

        return self.statement

    # negation
    def __neg__(self):
        """return negation of proposition
            returns:
                negation (Proposition)
        """

        # building object
        statement = "NOT {}".format(self.statement)
        truth = not self.truth
        negation = Proposition(statement, truth)

        return negation

    # conjunction
    def __and__(self, other):
        """return conjuction of two propositions
            args:
                other (Proposition)
            returns:
                conjuction (Proposition)
        """

        # building object
        statement = "{0} AND {1}".format(self.statement, other.statement)
        truth = self.truth and other.truth
        conjunction = Proposition(statement, truth)

        return conjunction

    # disjunction
    def __or__(self, other):
        """return disjuction of two propositions
            args:
                other (Proposition)
            returns:
                disjuction (Proposition)
        """

        # building object
        statement = "{0} OR {1}".format(self.statement, other.statement)
        truth = self.truth or other.truth
        disjunction = Proposition(statement, truth)

        return disjunction

    # implication
    def __rshift__(self, other):
        """return implication of one proposition to another
            args:
                other (Proposition)
            returns:
                implication (Proposition)
        """

        # building object
        statement = "{0} IMPLIES {1}".format(self.statement, other.statement)
        truth = not self.truth or other.truth
        implication = Proposition(statement, truth)

        return implication

class FuzzyProposition(Proposition):
    """statement in a fuzzy propositional calculus
        inheritance:
            Proposition
        attributes:
            statement (str)
            truth (0 <= float <=1 or None) [default=None]
        methods:
            __init__ -- instantiation
                args:
                    statement (str)
                    truth (0 <= float <= 1 or None) [default=None]
            __repr__ -- representation
                returns:
                    rep (str)
            __neg__ -- negation
                returns
                    negation (FuzzyProposition)
            __and__ -- conjunction
                args:
                    other (FuzzyProposition)
                returns
                    conjunction (FuzzyProposition)
            __or__ -- disjunction
                args:
                    other (FuzzyProposition)
                returns
                    disjunction (FuzzyProposition)
            __rshift__ -- implication
                args:
                    other (FuzzyProposition)
                returns
                    implication (FuzzyProposition)
    """

    # instantiation
    def __init__(self, statement, truth=None):
        """instantiate a statement in the fuzzy propositional calculus
            args:
                statement (str)
                truth (0 <= float <= 1 or None) [default=None]
        """

        # calling super
        super().__init__(statement, truth)

    # string representation
    def __repr__(self):
        """represent fuzzy proposition as a string
            returns:
                rep (str)
        """

        return super().__repr__()

    # negation
    def __neg__(self):
        """return negation of fuzzy proposition
            returns:
                negation (FuzzyProposition)
        """

        # building object
        statement = "NOT {}".format(self.statement)
        if self.truth is None:
            truth = None
        else:
            truth = 1 - self.truth
        negation = FuzzyProposition(statement, truth)

        return negation

    # conjunction
    def __and__(self, other):
        """return conjuction of two fuzzy propositions
            args:
                other (FuzzyProposition)
            returns:
                conjuction (FuzzyProposition)
        """

        # building object
        statement = "{0} AND {1}".format(self.statement, other.statement)
        if self.truth is None or other.truth is None:
            truth = None
        else:
            truth = min(self.truth, other.truth)
        conjunction = FuzzyProposition(statement, truth)

        return conjunction

    # disjunction
    def __or__(self, other):
        """return disjuction of two fuzzy propositions
            args:
                other (FuzzyProposition)
            returns:
                disjuction (FuzzyProposition)
        """

        # building object
        statement = "{0} OR {1}".format(self.statement, other.statement)
        if self.truth is None or other.truth is None:
            truth = None
        else:
            truth = max(self.truth, other.truth)
        disjunction = FuzzyProposition(statement, truth)

        return disjunction

    # implication
    def __rshift__(self, other):
        """return implication of one fuzzy proposition to another
            args:
                other (FuzzyProposition)
            returns:
                implication (FuzzyProposition)
        """

        # building object
        statement = "{0} IMPLIES {1}".format(self.statement, other.statement)
        if self.truth is None or other.truth is None:
            truth = None
        else:
            truth = max((-self).truth, other.truth)
        implication = FuzzyProposition(statement, truth)

        return implication
