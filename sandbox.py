"""
sandbox for designing, building, and testing blocks of code
"""

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
    def __init__(self, bottom_value=None, limit=None):
        """
        instantiate a LIFO stack
            parameters:
                bottom_value (any type) [default=None]
                limit (int > 0 or None) [default=None]
        """
        
        #this attribute represents the top item
        #the value _init_ially stored is the first_in element,
        #the bottom of the stack
        self.top_item = Node(bottom_value)

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
        if self.top_item is not None:
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
        if self.top_item is not None:
            value = self.top_item.value

        #otherwise print error message
        else:
            print("Stack is empty")
            return None
            
        return value

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
                bottom_value
                limit
