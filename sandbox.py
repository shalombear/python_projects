"""
sandbox for designing, building, and testing blocks of code
"""


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
