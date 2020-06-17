"""
graph BFS:
word ladder
Transform the word “FOOL” into the word “SAGE”. In a word ladder puzzle you must make the change occur gradually by changing one letter at a time.
FOOL
POOL
POLL
POLE
PALE
SALE
SAGE

Represent the relationships between the words as a graph.

Use the graph algorithm known as breadth first search to find an efficient path from the starting word to the ending word.

Suppose that we have a huge number of buckets, each of them with a four-letter word on the outside, except that one of the letters in the label has been replaced by an underscore. (POP_  P_PE  PO_E  _OPE)

As we process each word in our list we compare the word with each bucket, using the ‘_’ as a wildcard, so both “pope” and “pops” would match “pop_.” Every time we find a matching bucket, we put our word in that bucket. Once we have all the words in the appropriate buckets we know that all the words in the bucket must be connected.

The graph algorithm we are going to use is called the “breadth first search” algorithm. 

Given a graph 𝐺 and a starting vertex 𝑠, a breadth first search proceeds by exploring edges in the graph to find all the vertices in 𝐺 for which there is a path from 𝑠. 

This new vertex class adds three new instance variables: distance, predecessor, and color. 

To keep track of its progress, BFS colors each of the vertices white, gray, or black. All the vertices are initialized to white when they are constructed. A white vertex is an undiscovered vertex. When a vertex is initially discovered it is colored gray, and when BFS has completely explored a vertex it is colored black. This means that once a vertex is colored black, it has no white vertices adjacent to it. 

BFS begins at the starting vertex s and colors start gray to show that it is currently being explored. Two other values, the distance and the predecessor, are initialized to 0 and None respectively for the starting vertex.

Finally, start is placed on a Queue. The next step is to begin to systematically explore vertices at the front of the queue. We explore each new node at the front of the queue by iterating over its adjacency list.

If it is white, the vertex is unexplored, and four things happen:

- The new, unexplored vertex nbr, is colored gray.

- The predecessor of nbr is set to the current node currentVert

- The distance to nbr is set to the distance to currentVert + 1

- nbr is added to the end of a queue. Adding nbr to the end of the queue effectively schedules this node for further exploration, but not until all the other vertices on the adjacency list of currentVert have been explored.

"""
from Graph import Graph, Vertex
from Queue import Queue

def buildGraph(wordFile):
    d = {}
    g = graph()
    wfile = open(wordFile, 'r')
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = word

    # build graph to connect words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word1)
    return g

# Breadth first search for finding the unweighted shortest path.
def bfs(g,start):  # 𝑂(𝑉+𝐸)
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while (vertQueue.size() > 0):
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if (nbr.getColor() == 'white'):
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')

def traverse(y):
    x = y
    while (x.getPred()):
        print(x.getId())
        x = x.getPred()
    print(x.getId())

traverse(g.getVertex('sage'))

if __name__ == '__main__':
    print(buildGraph(wordFile))

