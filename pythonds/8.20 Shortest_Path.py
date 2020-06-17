"""
Graph:
Dijkstra’s algorithm for weighted shortest path.
Shortest Path Problems (shortest path from start node to other nodes):
The problem that we want to solve is to find the path with the smallest total weight along which to route any given message.

To keep track of the total cost from the start node to each destination we will make use of the dist instance variable in the Vertex class. 

The value that is used to determine the order of the objects in the priority queue is dist. When a vertex is first created dist is set to a very large number. 


"""
from Graph import Graph, Vertex
from Minheap import BinHeap


def dijkstra(aGraph,start): # 𝑂((𝑉+𝐸)log(𝑉))
    pq = BinHeap()
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in aGraph])  # 𝑂(𝑉)
    while not pq.isEmpty():
        currentVert = pq.delMin()  # 𝑂(𝑉log(𝑉))
        for nextVert in currentVert.getConnections():
            # total weight 
            newDist = currentVert.getDistance() + currentVert.getWeight(nextVert)
            if newDist < nextVert.getDistance():  # +inf in the beginning
                nextVert.setDistance( newDist )
                nextVert.setPred(currentVert)
                # decreaseKey is used when the distance to a vertex that is already in the queue is reduced, and thus moves that vertex toward the front of the queue.
                pq.decreaseKey(nextVert,newDist)  # 𝑂(𝐸log(𝑉))
