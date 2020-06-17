"""
Graph:
Graph() creates a new, empty graph.
addVertex(vert) adds an instance of Vertex to the graph.
addEdge(fromVert, toVert) Adds a new, directed edge to the graph that connects two vertices.
addEdge(fromVert, toVert, weight) Adds a new, weighted, directed edge to the graph that connects two vertices.
getVertex(vertKey) finds the vertex in the graph named vertKey.
getVertices() returns the list of all vertices in the graph.
in returns True for a statement of the form vertex in graph, if the given vertex is in the graph, False otherwise.

"""

# using adjacent list to implement Graph
# Each Vertex uses a dictionary to keep track of the vertices to which it is connected, and the weight of each edge.

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    # The getConnections method returns all of the vertices in the adjacency list
    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]

# graph: contains a dictionary that maps vertex names to vertex objects.

class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            fv = self.addVertex(f)
        if t not in self.vertList:
            tv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    # The getVertices method returns the names of all of the vertices in the graph
    def getVertices(self):
        return self.vertList.keys()

    # The __iter__ method to make it easy to iterate over all the vertex objects in a particular graph.
    def __iter__(self):
        return iter(self.vertList.values())

if __name__ == '__main__':
    g = Graph()
    """
    for i in range(6):
        g.addVertex(i)
    """
    print(g.vertList)
    g.addEdge(0,1,5)
    g.addEdge(0,5,2)
    g.addEdge(1,2,4)
    g.addEdge(2,3,9)
    g.addEdge(3,4,7)
    g.addEdge(3,5,3)
    g.addEdge(4,0,1)
    g.addEdge(5,4,8)
    g.addEdge(5,2,1)
    print(g.vertList)
    print(g.getVertices())
    print(g.numVertices)

    print(g.getVertex(0))
    # return self.vertList[0] -> 0 vertex object -> 
    # return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    for v in g: # return iter(self.vertList.values())
        for w in v.getConnections():  # w is keys in the dictionary
            print("(%s, %s, %s)" % (v.getId(), w.getId(), v.getWeight(w)))



