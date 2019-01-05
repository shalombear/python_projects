"""
accept input from user
determine if input is a valid Roman numeral
    if it is, print equivalent in Arabic numerals
    otherwise, print location of violation in input string

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

    Queue -- a FIFO queue
        attributes:
            head (Node or None)
            tail (Node or None)
            size (int >= 0)


    RomanNum -- a Roman numeral
        attributes:
            numeral (str)
            value (int)
        methods:
            __init__ -- instantiation
                args:
                    numeral (str)
                    value (int)
            __repr__ -- string representation
                returns:
                    numeral (str)
            __lt__ -- order
                args:
                    other (RomanNum)
                returns:
                    less (bool)
            __eq__ -- equality
                args:
                    other (RomanNum)
                returns:
                    equal (bool)
                    
"""

# importing libraries
from tkinter import *

# importing functions
from functools import total_ordering


# the Node class is used to implement linked list data structures
class Node:
    """
    a node in a linked list
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

        # assigning attributes
        self.value = value
        self.link_node = link_node

    # representation
    def __repr__(self):
        """represent node object as a string
            returns:
                rep (str)
        """

        # constructing the representation
        if self.link_node is None:
            linker = '(unlinked node)'
        else:
            linker = self.link_node.value
        rep = "Data: \t{0}\nLink: \t{1}".format(self.value, linker)

        return rep

    # linking a node
    def set_link(self, link_node):
        """assign a link to a node
            args:
                link_node (Node)
        """
        
        self.link_node = link_node

    # retrieving a linked node
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


class Queue:
    """
    a FIFO queue
        attributes:
            head (Node or None)
            tail (Node or None)
            size (int >= 0)
        methods:
            __init__ -- instantiation
            __repr__ -- string representation
                returns:
                    rep (str)
            is_empty -- helper method
                returns:
                    empty (bool)
            peek -- return head without removing from queue
                returns:
                    
            enqueue -- add tail
            dequeue -- remove head and return
    """

    # instantiation
    def __init__(self):
        """instantiate a queue"""

        # queue is intitialized in empty state
        # assigning attributes
        self.head = None
        self.tail = None
        self.size = 0

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
        """add a node to the queue
            args:
                
        """

        new_item = Node(value)

        if self.is_empty():
            self.head = new_item

        else:
            self.tail.set_link(new_item)

        self.tail = new_item
        self.size += 1

    def dequeue(self):

        if not self.is_empty():
            value = self.head.value
            self.head = self.head.get_link()
            self.size -= 1
            return value

        else:
            return None
    
@total_ordering
class RomanNum:
    """a Roman numeral"""

    # instantiation
    def __init__(self, numeral, value):
        """instantiate a Roman numeral object
            args:
                numeral (str)
                value (int)
        """

        # assigning attributes
        self.numeral = numeral
        self.value = value

    # string representation
    def __repr__(self):
        """represent Roman numeral object as string
            returns:
                numeral (str)
        """

        return self.numeral

    # order
    def __lt__(self, other):
        """check order of two Roman numeral objects
            args:
                other (RomanNum)
            returns:
                less (bool)
        """

        less = self.value < other.value
        return less

    # equality
    def __eq__(self, other):
        """compare values of two Roman numeral objects
            args:
                other (RomanNum)
            returns:
                equal (bool)
        """

        equal = self.value == other.value
        return equal


# # # # # # # # # # # # # # # # # # # # # # # # #
### PROGRAM OUTLINE

# a dictionary containing the Roman numerals and their representative values
roman_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }

# get user input

entry = input("gimme a Roman number: ").upper()

print(entry)

# enqueue the string, each node's value is a RomanNum object

roman_number = Queue()

for symbol in entry:
    if symbol in roman_dict.keys():
        roman_number.enqueue(RomanNum(symbol, roman_dict[symbol]))


# raise error if input contains invalid symbol

    else:
        raise ValueError

# separate function to check syntactics here
# functionally functioning functional function
def syntax_checker(entry):
    """check if entry is syntactic"""

    ones = ['I', 'X', 'C', 'M']
    fives = ['V', 'L', 'D']

    # string methods

    # no more than three consecutive ones
    for i in ones:
        if i*4 in entry:
            raise ValueError

    # no more than one consecutive five
    for v in fives:
        if v*2 in entry:
            raise ValueError

# run syntax check
syntax_checker(entry)

# set toggle switch off

minus_toggle = False
trash_can = []

# initialize return value
arabic_number = 0

# loop until string is read

while not roman_number.is_empty():

## read symbol

    current_symbol = roman_number.dequeue()
    if current_symbol in trash_can:
        raise ValueError    

    next_symbol = roman_number.peek()
    if next_symbol is None:
        next_symbol = RomanNum('O', 0)

## check that next symbol is of equal or lesser value

    if next_symbol > current_symbol:

## if not, and switch not toggled, toggle switch and subtract
        if minus_toggle == False:
            minus_toggle = True
            arabic_number -= current_symbol.value
            trash_can.append(current_symbol)

## if not, and switch is toggled, raise error
        else:
            raise ValueError

## if so, untoggle switch and add
    else:
        minus_toggle = False
        arabic_number += current_symbol.value

print(arabic_number)
