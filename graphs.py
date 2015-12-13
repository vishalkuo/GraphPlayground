import Queue as q

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}



"""
DEPTH-FIRST SEARCH
"""
def publicDFS(G, key):
    DFS(G, key, set())    

def DFS(G, key, visitedSet):
    print(key)
    visitedSet.add(key)
    for item in G[key]:
        if item not in visitedSet:
            DFS(G, item, visitedSet)
    # Print call can alternatively be here

"""
BREADTH-FIRST SEARCH
"""
def publicBFS(G, key):
    BFS(G, key, set(), q.Queue())

def BFS(G, key, visitedSet, queue):
    visitedSet.add(key)
    queue.put(key)
    while queue.qsize > 0:
        v = queue.get()
        print v
        for item in G[v]:
            if item not in visitedSet:
                queue.put(item)
                visitedSet.add(item)


print("DFS WITH C AS ROOT")
publicDFS(graph, 'C')
print("BFS WITH C AS ROOT")
publicBFS(graph, 'C')
