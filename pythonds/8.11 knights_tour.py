"""
Graph:
knight’s tour
The object of the puzzle is to find a sequence of moves that allow the knight to visit every square on the board exactly once. 

- Represent the legal moves of a knight on a chessboard as a graph.

- Use a graph algorithm to find a path of length 𝑟𝑜𝑤𝑠×𝑐𝑜𝑙𝑢𝑚𝑛𝑠−1 where every vertex on the graph is visited exactly once.

To represent the knight’s tour problem as a graph we will use the following two ideas: Each square on the chessboard can be represented as a node in the graph. Each legal move by the knight can be represented as an edge in the graph.

The search algorithm we will use to solve the knight’s tour problem is called depth first search (DFS).

The first algorithm we will look at directly solves the knight’s tour problem by explicitly forbidding a node to be visited more than once. 

"""
from Graph import Graph, Vertex

def knightGraph(bdsize):
    ktGraph = Graph()
    for row in range(bdsize):
        for col in range(bdsize):
            nodeId = posToNodeId(row, col, bdsize)
            newPositions = genLegalMoves(row, col, bdsize)
            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdsize)
                ktGraph.addEdge(nodeId, nid)
    return ktGraph

def posToNodeId(row, col, boardsize):
    return (row * boardsize) + col

def genLegalMoves(row, col, boardsize):
    newpositions = []
    steps = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
    for s in steps:
        newX = row + s[0]
        newY = col + s[1]
        if legalcoord(newX, boardsize) and legalcoord(newY, boardsize):
            newpositions.append((newX,newY))
    return newpositions

def legalcoord(x, boardsize):
    if x >= 0 and x < boardsize:
        return True
    else:
        return False

def knightTour(n,path,u,limit):  - O(k^n)
    # u, the vertex in the graph we wish to explore
    # n, the current depth in the search tree
    # path, a list of vertices visited up to this point
    # limit, the number of nodes in the path
    u.setColor('gray')
    path.append(u)  # stack 
    if n < limit:
        nbrList = list(u.getConnections()) # get adjecent vertex
        i = 0
        done = False
        while i < len(nbrList) and not done:
            if nbrList[i].getColor() == 'white': # never explored
                done = knightTour(n+1, path, nbrList[i], limit)
            i = i + 1
        # prepare to backtrack
        if not done:
            path.pop() 
            u.setColor('white')
    else:
        done = True
    return done


if __name__ == '__main__':
    g = knightGraph(5)
    print(g.vertList) # objects
    print(g.getVertices())
    print(g.numVertices)

    print(g.getVertex(12)) # where the knight can go if it is at 12.
