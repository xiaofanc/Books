"""
Graph: DFS - 𝑂(𝑉+𝐸)

The discovery time tracks the number of steps in the algorithm before a vertex is first encountered. The finish time is the number of steps in the algorithm after a vertex is colored black. 

we chose to implement the code as methods of a class that inherits from the Graph class.

This implementation extends the graph class by adding a time instance variable and the two methods dfs and dfsvisit.

"""
from Graph import Graph
class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)
        for aVertex in self:
            if aVertex.getColor() == 'white':
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)
        # explores all of the neighboring white vertices as deeply as possible.
        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white':
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)  # DFS
        startVertex.setColor('black') # without neighbors to be explored
        self.time += 1
        startVertex.setFinish(self.time)

