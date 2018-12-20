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
    """

    def __init__(self, value):
        """
        instantiate a TreeNode object
            parameters:
                value (any type)
        """

        self.value = value
        self.children = []

    def add_child(self, child):
        """
        add a child node
            parameters:
                child (TreeNode)
        """

        self.children.append(child)
