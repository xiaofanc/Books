"""
Graph: DFS
Topological Sorting
Topological sort for ordering tasks.
A topological sort takes a directed acyclic graph and produces a linear ordering of all its vertices such that if the graph 𝐺 contains an edge (𝑣,𝑤) then the vertex 𝑣 comes before the vertex 𝑤 in the ordering.

The topological sort is a simple but useful adaptation of a depth first search. The algorithm for the topological sort is as follows:

- Call dfs(g) for some graph g. The main reason we want to call depth first search is to compute the finish times for each of the vertices.
- Store the vertices in a list in decreasing order of finish time.
- Return the ordered list as the result of the topological sort.


Strongly Connected Components:
One graph algorithm that can help find clusters of highly interconnected vertices in a graph is called the strongly connected components algorithm (SCC). 


Shortest Path Problems:
The problem that we want to solve is to find the path with the smallest total weight along which to route any given message.

"""

