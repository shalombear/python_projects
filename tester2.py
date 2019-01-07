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
                value (any type)                
        """

        new_item = Node(value)

        if self.is_empty():
            self.head = new_item

        else:
            self.tail.set_link(new_item)

        self.tail = new_item
        self.size += 1

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
    
@total_ordering
class RomanNum:
    """a Roman numeral
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

# method to find a needle in a haystack
def find_nth(string, sub, n):
    """search a string and return the nth occurence of a substring
        args:
            string (str)
            sub (str)
            n (int > 0)
        returns:
            sub_idx (int >= 0)
    """

    # set dummy variable
    if sub[0] == 'i':
        replacer = 'j'
    else:
        replacer = 'i'

    # loop through n, find substring index, modify string, decrement n    
    while n > 0:
        sub_idx = string.find(sub)
        string = string[:sub_idx] + replacer + string[sub_idx + 1 :]
        n -= 1

    return sub_idx


# main function
def roman_numeral_computer(entry):
    """check if entry is syntactically valid as a roman number
        args:
            entry (str)
        returns:
            summand (int), or
            msg (str)
    """

    entry = entry.upper()
        
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

    # and a Queue object
    queue = Queue()
        
    # check if each symbol is a key in the dictionary
    for symbol in entry:

        # if so, use to construct and enqueue a RomanNum object
        if symbol in roman_dict.keys():
            numeral = RomanNum(symbol, roman_dict[symbol])
            queue.enqueue(numeral)

        # otherwise, raise error
        else:
            error_idx = find_nth(entry, symbol, 1)
            msg = 'Error in position {0}\n{1} is not a Roman numeral'
            msg = msg.format(error_idx, symbol)
            return msg
        
    # declare base case, cap, trash can, toggle switch, and summand
    last_symbol = RomanNum('O', 10**20)
    cap = last_symbol
    trash = []
    next_switch = False
    summand = 0

    while not queue.is_empty():
        

        # dequeue the first symbol and peek the next one
        current_symbol = queue.dequeue()
        # alias
        cur = current_symbol

        if not queue.is_empty():
            next_symbol = queue.peek()
        else:
            next_symbol = RomanNum('E', 0)

        # current symbol may not be in trash
        if cur in trash:
            error_idx = len(entry) - queue.size - 1
            msg = 'Error in position {0}\n{1} cannot be reused'
            msg = msg.format(error_idx, cur)
            return msg

        # current symbol may only exceed cap if switch is set
        # in which case add to summand, trash symbol, and reset switch
        if cur > cap:
            if next_switch:
                trash.append(cur)
                next_switch = False
            else:
                error_idx = len(entry) - queue.size - 1
                msg = 'Error in position {0}\n{1} may not be used here'
                msg = msg.format(error_idx, cur)
                return msg

        # next symbol may only exceed current if current symbol is subtractive,
        # less than last, not trashed, and not a five
        # in which case set cap, trash symbol, subtract value, set switch
        case = cur < last_symbol and cur not in trash and str(cur) not in fives
        if cur < next_symbol:
            if case:
                cap = cur
                trash.append(cur)
                summand -= cur.value
                next_switch = True
            else:
                error_idx = len(entry) - queue.size
                msg = 'Error in position {0}\n{1} may not be used here'
                msg = msg.format(error_idx, next_symbol)
                return msg

        # add symbol's value if it has not been subtracted
        if not next_switch:
            summand += cur.value

        # a five may not appear more than once
        if str(cur) in fives:
            trash.append(cur)        

        # set current symbol to last
        last_symbol = current_symbol

    # a one appearing more than thrice raises an error
    for i in ones:
        if entry.count(i) > 3:
            error_idx = find_nth(entry, i, 4)
            msg = 'Error in position {0}\nMaximum 1 instance of {1}'
            msg = msg.format(error_idx, i)
            return msg

    # if no error was raised, the Arabic numeral is returned
    return summand

from random import choice, randint
LIB = 'IVXLCDM'

for i in range(10):
    testnum = ""
    for j in range(randint(1,10)):
        testnum += choice(LIB)

    print("""\n\n*************************
Now testing: {0}\n
Test result:
{1}""".format(testnum, roman_numeral_computer(testnum)))
