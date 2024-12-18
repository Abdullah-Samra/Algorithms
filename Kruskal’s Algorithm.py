class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = [] 

    def add_edge(self, u, v, weight):
        self.edges.append((u, v, weight))

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])  
    return parent[x]

def union(parent, rank, x, y):
    rootX = find(parent, x)
    rootY = find(parent, y)

    if rootX != rootY:
        if rank[rootX] > rank[rootY]:
            parent[rootY] = rootX
        elif rank[rootX] < rank[rootY]:
            parent[rootX] = rootY
        else:
            parent[rootY] = rootX
            rank[rootX] += 1

def kruskal(graph):
    mst = []  
    graph.edges.sort(key=lambda edge: edge[2])  

    
    parent = [i for i in range(graph.vertices)]
    rank = [0] * graph.vertices

    for u, v, weight in graph.edges:
        
        if find(parent, u) != find(parent, v):
            mst.append((u, v, weight))
            union(parent, rank, u, v)

        if len(mst) == graph.vertices - 1:
            break

    return mst


g = Graph(4)
g.add_edge(0, 1, 10)
g.add_edge(0, 2, 6)
g.add_edge(0, 3, 5)
g.add_edge(1, 3, 15)
g.add_edge(2, 3, 4)

mst = kruskal(g)
print("Edges in MST:")
for u, v, weight in mst:
    print(f"({u}, {v}) - Weight: {weight}")
