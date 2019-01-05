
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



###################

def roman_numeral_computer(entry):
    """check if entry is syntactically valid as a roman number
        args:
            entry (str)
        returns:
            roman_number (int)
    """

    # a dictionary containing Roman numerals and their representative values
    roman_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }

    # some useful lists
    ones = ['I', 'X', 'C', 'M']
    fives = ['V', 'L', 'D']

    # and an object
    inqueue = Queue()

    # check if each symbol is a key in the dictionary

    # if it is, use it and its value to construct and enqueue a RomanNum object
    # onto the first queue

    # otherwise, raise error

    # count ones and fives in entry
    
    # a one appearing more than thrice or a five more than once raises an error

    # next, declare a second queue and iterate through the first one

    outqueue = Queue()

    # dequeue the first symbol and peek the next one

    # discards go in bin, declared here

    # if next symbol is less than or equal to current, proceed

        #symbol value is positive, symbol goes in bin, symbol goes on outqueue

    # otherwise

        # if current symbol is in bin, raise error

        # otherwise, proceed

            # symbol value is negative, symbol goes in bin, symbol goes on outcue

    # create summand

    # iterate through queue and compute summand

    # return summand
