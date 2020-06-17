"""
Graph:
Prim's Spanning Tree Algorithm

Minimum weight spanning trees for broadcasting messages.

Prim’s algorithm belongs to a family of algorithms called the “greedy algorithms” because at each step we will choose the cheapest next step. In this case the cheapest next step is to follow the edge with the lowest weight.

Prim’s algorithm is similar to Dijkstra’s algorithm in that they both use a priority queue to select the next vertex to add to the growing graph.

"""
from Graph import Graph, Vertex
from Minheap import BinHeap

def prim(G, start):
    pq = BinHeap()
    for v in G:
        # The distances to all the other vertices are initialized to infinity.
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(),v) for v in G])
    while not pq.isEmpty():
        currentVert = pq.delMin()  # part of the spanning tree 
        for nextVert in currentVert.getConnections():
            newcost = currentVert.getWeight(nextVert)
            # update distances 
            if nextVert in pq and newcost < nextVert.getDistance():
                nextVert.setDistance(newcost)
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert,newcost)



