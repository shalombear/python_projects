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

        # a vertex is represented by its value
        rep = str(self.value)
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
            rep += str(vertex)
            rep += ": "
            for v in vertex.get_edges():
                rep += str(v) +", "

            rep = rep[:-2]
            rep += "\n"

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

    # a method to find if there is a path in the graph between two vertices
    def has_path(self, v1, v2):
        """check if there is a path between two vertices
            args:
                v1 (Vertex)
                v2 (Vertex)
            returns:
                path (bool)
        """

        # list of nodes to visit, discard pile, and return variable
        start = [v1]
        visited = []
        path = False

        # looping as long as list is non-empty
        while start:

            # grabbing the working node out of the list
            # mark as visited and check if destination
            current = start.pop(0)
            visited.append(current)
            if current == v2:
                path = True
                start = []

            # otherwise extend the list of nodes to visit
            else:
                edges = [x for x in current.get_edges() if x not in visited]
                start.extend(edges)

        return path

        

# test variables
v1 = Vertex('spam')
v2 = Vertex('baked beans')
v3 = Vertex('egg')
v4 = Vertex('lobster thermidor')
v5 = Vertex('pining for the fjords')
v6 = Vertex('dead parrot')

v5.add_edge(v6)

v2.add_edge(v1)
v3.add_edge(v4)
v4.add_edge(v1)
v1.add_edge(v3)
g = Graph()
